# week2/reference — 강사 참조 솔루션

| 파일 | 회차 | 외부 의존 |
| --- | --- | --- |
| `01_loop_orderings.py` | [2-1](../sessions/2-1.md) | numpy |
| `02_tpu_systolic.py` | [2-2](../sessions/2-2.md) | numpy |
| `03_stationary_compare.py` | [2-3](../sessions/2-3.md) | numpy |
| `04_integrated_compare.py` | [2-4](../sessions/2-4.md) | numpy, matplotlib |

> 2-5는 학생이 *분석*하는 회차라 reference 코드가 작음. 학생이 자유롭게 작성.

## 실행

```bash
source ../../.venv/bin/activate
cd week2/reference
python 01_loop_orderings.py
python 02_tpu_systolic.py
python 03_stationary_compare.py
python 04_integrated_compare.py
```

## 핵심 알고리즘 노트

### 02 — Systolic array 출력 매핑 공식

Weight stationary, K rows × N cols PE array, M×K×N MatMul:

- 입력 schedule: `A[m, k]` → PE[k, 0] at cycle `t = m + k`
- 출력: `C[m, n]` → bottom-row PE[K-1, n] emerges at cycle `t = m + K + n`
- 총 사이클: `M + K + N - 1`

(증명/검증은 작은 예제로 cycles_outputs[2][0]에 C[0,0]가 나오는지 trace.)
