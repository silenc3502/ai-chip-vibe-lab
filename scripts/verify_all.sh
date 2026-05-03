#!/usr/bin/env bash
# verify_all.sh — 모든 reference 솔루션 회귀 검증
#
# 실행:
#   scripts/verify_all.sh           # 전체
#   scripts/verify_all.sh week3     # 특정 주차만
#
# 종료 코드: 0 = 모두 통과, 1 = 하나 이상 실패

set -u
cd "$(dirname "$0")/.."

if [ ! -d ".venv" ]; then
    echo "❌ .venv 없음. SETUP.md §3 참고해서 venv 생성 후 재시도."
    exit 1
fi

# shellcheck disable=SC1091
source .venv/bin/activate

FILTER="${1:-all}"
PASS=0
FAIL=0
FAILURES=()

run_python() {
    local name=$1
    local file=$2
    local dir
    dir=$(dirname "$file")
    local base
    base=$(basename "$file")
    printf "  %-40s " "$name"
    if (cd "$dir" && python "$base" > /tmp/verify_all.log 2>&1); then
        echo "✓"
        PASS=$((PASS+1))
    else
        echo "✗ (see /tmp/verify_all.log)"
        FAIL=$((FAIL+1))
        FAILURES+=("$name")
    fi
}

run_make() {
    local name=$1
    local dir=$2
    printf "  %-40s " "$name"
    if (cd "$dir" \
        && rm -rf sim_build results.xml dump.vcd __pycache__ \
        && make > /tmp/verify_all.log 2>&1 \
        && grep -q "FAIL=0" /tmp/verify_all.log); then
        echo "✓"
        PASS=$((PASS+1))
        rm -rf "$dir/sim_build" "$dir/results.xml" "$dir/dump.vcd" "$dir/__pycache__"
    else
        echo "✗ (see /tmp/verify_all.log)"
        FAIL=$((FAIL+1))
        FAILURES+=("$name")
    fi
}

if [[ "$FILTER" == "all" || "$FILTER" == "week1" ]]; then
    echo "=== Week 1 ==="
    run_python "1-1 loop_vs_numpy"      "week1/reference/01_loop_vs_numpy.py"
    run_python "1-2 cache_effect"       "week1/reference/02_cache_effect.py"
    run_python "1-3 simd_intro"         "week1/reference/03_simd_intro.py"
    run_python "1-4 matmul_baseline"    "week1/reference/04_matmul_baseline.py"
    run_python "1-5 cpu_gpu_npu"        "week1/reference/05_cpu_gpu_npu.py"
fi

if [[ "$FILTER" == "all" || "$FILTER" == "week2" ]]; then
    echo "=== Week 2 ==="
    run_python "2-1 loop_orderings"     "week2/reference/01_loop_orderings.py"
    run_python "2-2 tpu_systolic"       "week2/reference/02_tpu_systolic.py"
    run_python "2-3 stationary_compare" "week2/reference/03_stationary_compare.py"
    run_python "2-4 integrated_compare" "week2/reference/04_integrated_compare.py"
fi

if [[ "$FILTER" == "all" || "$FILTER" == "week3" ]]; then
    echo "=== Week 3 (Python) ==="
    run_python "3-1 npu_config"         "week3/reference/01_npu_config.py"
    run_python "3-2 mac_and_memory"     "week3/reference/02_mac_and_memory.py"
    run_python "3-3 npu_simulator"      "week3/reference/03_npu_simulator.py"
    run_python "3-4 npu_perf"           "week3/reference/04_npu_perf.py"
    run_python "3-5 npu_optimize"       "week3/reference/05_npu_optimize.py"
    echo "=== Week 3 (Verilog/cocotb) ==="
    run_make   "3-2 mac.v cocotb tests" "week3/reference/02_mac_verilog"
    run_make   "3-4 cycle_compare"      "week3/reference/04_cycle_compare"
fi

if [[ "$FILTER" == "all" || "$FILTER" == "week4" ]]; then
    echo "=== Week 4 ==="
    run_python "4-1 pareto_front"       "week4/reference/01_pareto_front.py"
    run_python "4-2 perf_axes"          "week4/reference/02_perf_axes.py"
    run_python "4-3 app_workload"       "week4/reference/03_app_workload.py"
    run_python "4-4 scenario_tuning"    "week4/reference/04_scenario_tuning.py"
fi

echo ""
echo "=================================="
echo "  PASS: $PASS"
echo "  FAIL: $FAIL"
if [ $FAIL -gt 0 ]; then
    echo ""
    echo "Failures:"
    for f in "${FAILURES[@]}"; do
        echo "  - $f"
    done
    exit 1
fi
echo "=================================="
