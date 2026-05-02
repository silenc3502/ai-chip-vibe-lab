# week1/reference — 강사 참조 솔루션

각 회차의 *최소 통과 기준*을 만족하는 reference 구현입니다. 학생이 막혔을 때 분기시키거나 채점 기준으로 사용합니다.

| 파일 | 회차 | 외부 의존 |
| --- | --- | --- |
| `01_loop_vs_numpy.py` | [1-1](../sessions/1-1.md) | numpy |
| `02_cache_effect.py` | [1-2](../sessions/1-2.md) | numpy, matplotlib |
| `03_simd_intro.py` | [1-3](../sessions/1-3.md) | numpy (+ py-cpuinfo optional) |
| `04_matmul_baseline.py` | [1-4](../sessions/1-4.md) | numpy |
| `05_cpu_gpu_npu.py` | [1-5](../sessions/1-5.md) | numpy, matplotlib |

## 학생 분기 가이드 (강사용)

학생이 막혔을 때 *전체 파일* 을 보여주지 말고 다음 기준으로 분기:

| 막힌 단계 | 보여줄 부분 |
| --- | --- |
| 함수 시그니처를 못 정함 | 함수 def 라인만 |
| 측정 방법론 (warmup, 평균) | `time_function` 또는 timing 패턴 부분만 |
| 검증 (allclose) | assert 라인만 |
| 시각화 | matplotlib 코드 블록 |
| 전체가 막힘 | 1단계씩 페어 코딩 |

## 실행

레포 루트에서:

```bash
source .venv/bin/activate
cd week1/reference
python 01_loop_vs_numpy.py
python 02_cache_effect.py
python 03_simd_intro.py
python 04_matmul_baseline.py
python 05_cpu_gpu_npu.py
```

## 참조 기기

macOS Apple Silicon (M2-class) 에서 검증. 다른 기기에서 절대값은 달라도 *비율*과 *경향*은 일치해야 합니다 (예: 1-1의 speedup이 100x 이상, 1-3의 (b)/(c) 비율이 100x 이상).
