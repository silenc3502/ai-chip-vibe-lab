# week3/lab

학생이 3주차 동안 만드는 코드. 본인 NPU 의 *누적 산출물* — Python 시뮬레이터 + Verilog RTL.

## 디렉토리 구조

```
week3/lab/
├── 01_npu_config.py            # NPUConfig dataclass (3-1)
├── 02_mac.py                   # Python MACUnit (3-2 Block 2)
├── 02_mac_verilog/             # Verilog MAC + cocotb (3-2 Block 3)
│   ├── mac.v
│   ├── test_mac.py
│   └── Makefile
├── 03_npu_simulator.py         # NPU 통합 시뮬 (3-3)
├── test_npu.py                 # 4 unit tests (3-3)
├── 04_npu_perf.py              # 5 워크로드 측정 (3-4)
├── 04_cycle_compare/           # RTL ↔ Python cycle 비교 (3-4)
│   ├── Makefile                # ../02_mac_verilog/mac.v 재사용
│   └── test_cycle_compare.py
└── 05_npu_optimize.py          # 1회 변경 + 재측정 (3-5)
```

## 회차별

| 회차 | 추가 / 변경 | 비고 |
| --- | --- | --- |
| 3-1 | `01_npu_config.py` | NPU 설계 결정 (코드 거의 안 씀) |
| 3-2 | `02_mac.py` + `02_mac_verilog/` | **첫 RTL 작성**, primer 사전 학습 권장 |
| 3-3 | `03_npu_simulator.py` + `test_npu.py` | 통합 시뮬 + 4 unit tests |
| 3-4 | `04_npu_perf.py` + `04_cycle_compare/` | 측정 + RTL 사이클 비교 |
| 3-5 | `05_npu_optimize.py` | 1회 변경 + 재측정 |

## 실행

```bash
source ../../.venv/bin/activate

# Python 시뮬
python 03_npu_simulator.py    # 4 unit tests
python 04_npu_perf.py         # 5 워크로드 측정

# Verilog (cocotb)
cd 02_mac_verilog && make     # 4 cocotb tests
cd ../04_cycle_compare && make  # RTL ↔ Python cycle 비교
```

## 참조 솔루션

`../reference/` 에 강사용 reference. 회차 종료 후 공개. 학생 막힘 시 step-by-step 분기 가이드는 `../reference/02_mac_verilog/README.md` 등 참고.
