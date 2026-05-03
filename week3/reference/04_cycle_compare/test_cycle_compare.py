"""Cycle-count comparison: Python NPU model prediction vs RTL actual.

Workload: K=1024 INT8 dot product on the MAC from 02_mac_verilog/mac.v.
For a fair comparison we configure Python NPU with 1×1 PE array (single MAC).

Pedagogical points:
  - Both compute the SAME accumulated value (correctness checked).
  - Python's analytical model includes a 1 μs dispatch overhead (= 1000 cycles at 1 GHz).
  - RTL pure compute is K cycles (one MAC per cycle) + a few cycles for reset/settle.
  - The cycle *ratio* shows where the abstraction differs.
"""
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

import cocotb
import numpy as np
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge
from cocotb.utils import get_sim_time

# Import Python NPU machinery from week3/reference/
_W3 = Path(__file__).parent.parent


def _import(name: str, fname: str):
    spec = spec_from_file_location(name, str(_W3 / fname))
    mod = module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


_cfg_mod = _import("npu_config_mod", "01_npu_config.py")
_sim_mod = _import("npu_sim_mod", "03_npu_simulator.py")

make_reference_config = _cfg_mod.make_reference_config
NPU = _sim_mod.NPU


@cocotb.test()
async def test_dot_product_1024_cycle_compare(dut):
    K = 1024
    rng = np.random.default_rng(0)
    a = rng.integers(-50, 50, K, dtype=np.int8)
    b = rng.integers(-50, 50, K, dtype=np.int8)
    expected = int(np.dot(a.astype(np.int32), b.astype(np.int32)))

    # Start 100 MHz clock
    PERIOD_NS = 10
    cocotb.start_soon(Clock(dut.clk, PERIOD_NS, "ns").start())

    # Reset
    dut.rst.value = 1
    dut.in_data.value = 0
    dut.weight.value = 0
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)
    dut.rst.value = 0
    await RisingEdge(dut.clk)

    # Begin compute window
    start_ns = get_sim_time(unit="ns")

    for av, bv in zip(a, b):
        dut.in_data.value = int(av)
        dut.weight.value = int(bv)
        await RisingEdge(dut.clk)

    # Settle one more cycle for the last MAC to land in acc
    dut.in_data.value = 0
    dut.weight.value = 0
    await RisingEdge(dut.clk)

    end_ns = get_sim_time(unit="ns")
    rtl_cycles = int(round((end_ns - start_ns) / PERIOD_NS))
    rtl_acc = dut.acc.value.to_signed()

    # Python NPU prediction with equivalent 1×1 PE
    cfg = make_reference_config()
    cfg.pe_array_rows = 1
    cfg.pe_array_cols = 1
    cfg.name = "edu-NPU 1×1 (single MAC)"
    npu = NPU(cfg)
    A = a.reshape(1, K)
    B = b.reshape(K, 1)
    py_r = npu.run(A, B)
    py_cycles = py_r.cycles
    py_acc = int(py_r.C[0, 0])

    cocotb.log.info("=" * 60)
    cocotb.log.info(f"K = {K} INT8 dot product on a single MAC unit")
    cocotb.log.info("=" * 60)
    cocotb.log.info(f"  RTL    : {rtl_cycles:>6} cycles, acc = {rtl_acc}")
    cocotb.log.info(f"  Python : {py_cycles:>6} cycles (predicted), acc = {py_acc}")
    cocotb.log.info(f"  NumPy ground truth                         acc = {expected}")
    cocotb.log.info(f"  Cycle ratio (Python_predicted / RTL_actual): "
                    f"{py_cycles / rtl_cycles:.2f}×")
    cocotb.log.info(f"  Note: Python model = compute + 1 μs dispatch overhead (1000 cy @ 1 GHz)")
    cocotb.log.info(f"        RTL pure compute = K cycles + a few for reset/settle")

    # Correctness — both must compute the right value
    assert rtl_acc == expected, f"RTL acc {rtl_acc} != ground truth {expected}"
    assert py_acc == expected, f"Python NPU acc {py_acc} != ground truth {expected}"

    # Cycle sanity: RTL should be roughly K cycles (within tight bound)
    assert K <= rtl_cycles <= K + 5, f"RTL cycles {rtl_cycles} outside [K, K+5] = [{K}, {K+5}]"

    # Python model should overestimate due to overhead model — that's the lesson
    assert py_cycles >= rtl_cycles, (
        f"Python model {py_cycles} should be >= RTL {rtl_cycles} due to overhead modeling"
    )
