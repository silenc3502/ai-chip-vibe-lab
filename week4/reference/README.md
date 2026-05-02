# week4/reference — 강사 참조 솔루션

| 파일 | 회차 | 외부 의존 |
| --- | --- | --- |
| `01_pareto_front.py` | [4-1](../sessions/4-1.md) | numpy, matplotlib + week3 NPU |
| `02_perf_axes.py` | [4-2](../sessions/4-2.md) | numpy, matplotlib + week3 NPU |
| `03_app_workload.py` | [4-3](../sessions/4-3.md) | numpy + week3 NPU |
| `04_scenario_tuning.py` | [4-4](../sessions/4-4.md) | numpy, matplotlib + week3 NPU |

> 4-5는 학생 발표 회차 — 코드 산출물 없음.

## 실행

```bash
source ../../.venv/bin/activate
cd week4/reference
python 01_pareto_front.py
python 02_perf_axes.py
python 03_app_workload.py
python 04_scenario_tuning.py
```

## Week 3 reference 의존

이 솔루션들은 `week3/reference/{01_npu_config,03_npu_simulator}.py`를 dynamic-import해서 사용합니다 (number-prefix 파일을 import 하기 위해 `importlib.util.spec_from_file_location`).

각 파일 상단의 `_import_local` 헬퍼가 같은 패턴.
