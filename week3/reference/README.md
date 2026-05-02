# week3/reference — 강사 참조 솔루션

| 파일 | 회차 | 외부 의존 |
| --- | --- | --- |
| `01_npu_config.py` | [3-1](../sessions/3-1.md) | (stdlib only) |
| `02_mac_and_memory.py` | [3-2](../sessions/3-2.md) | numpy |
| `03_npu_simulator.py` | [3-3](../sessions/3-3.md) | numpy |
| `04_npu_perf.py` | [3-4](../sessions/3-4.md) | numpy, matplotlib |
| `05_npu_optimize.py` | [3-5](../sessions/3-5.md) | numpy |

## 실행 순서

```bash
source ../../.venv/bin/activate
cd week3/reference
python 01_npu_config.py    # 자체 검증 + sample config 출력
python 02_mac_and_memory.py
python 03_npu_simulator.py # 4개 단위 테스트
python 04_npu_perf.py      # 5 워크로드 측정 + 차트
python 05_npu_optimize.py  # 변경 전/후 비교
```

## 참조 NPU 사양 (예시)

```python
NPUConfig(
    name="edu-NPU-v1",
    defining_feature="INT8 + 16MB SRAM, 16x16 systolic for batched inference",
    dtype="int8", dtype_bytes=1,
    pe_array_rows=16, pe_array_cols=16,
    dataflow="WS",
    clock_ghz=1.0,
    sram_kb=16_384,
    dram_bw_gbps=200,
    target_workload="LLM batched inference",
)
```

이 config는 16×16 INT8 PE = 256 lane × 1GHz × 2(MAC=2ops) = **512 GOPS peak**.
