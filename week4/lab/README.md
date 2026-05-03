# week4/lab

학생이 4주차 동안 만드는 코드. 본인 NPU 의 *최적화* + *응용 튜닝*.

## 디렉토리 구조

```
week4/lab/
├── 01_pareto_front.py        # 48 config DSE sweep + Pareto (4-1)
├── 02_perf_axes.py           # batching curve + cost 모델 (4-2)
├── 03_app_workload.py        # 3 응용 워크로드 + 측정 (4-3)
├── 04_scenario_tuning.py     # base vs tuned 비교 (4-4)
└── (선택) yosys_synth/       # 4-2 선택 도전 (yosys 합성)
```

## 회차별

| 회차 | 파일 | 비고 |
| --- | --- | --- |
| 4-1 | `01_pareto_front.py` | 4 SRAM × 4 PE × 3 dtype = 48 config sweep |
| 4-2 | `02_perf_axes.py` | latency/throughput curve + die area / power 모델. yosys 선택 도전 |
| 4-3 | `03_app_workload.py` | 자율주행 / 챗봇 / 영상 워크로드 — 본인 NPU 측정 |
| 4-4 | `04_scenario_tuning.py` | 선택 응용 튜닝 + specialization_efficiency 계산 |
| 4-5 | (코드 X) | 발표 + 피어 리뷰 + 코스 회고 |

## Week 3 산출물 의존

본 주차 모든 스크립트는 Week 3 의 NPUConfig / NPU 클래스를 import. 본인 `week3/lab/{01_npu_config, 03_npu_simulator}.py` 가 동작해야 함.

## 실행

```bash
source ../../.venv/bin/activate

python 01_pareto_front.py     # ~2분 (48 config × 시뮬)
python 02_perf_axes.py        # ~30초 (10 batch × 시뮬)
python 03_app_workload.py     # ~30초 (3 응용)
python 04_scenario_tuning.py  # ~1분 (base + tuned × 3 응용)
```

## 참조 솔루션

`../reference/` — 4 .py + 3 PNG. 단 4-5 는 발표 회차라 reference 코드 없음.
