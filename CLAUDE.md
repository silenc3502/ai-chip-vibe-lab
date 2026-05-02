# CLAUDE.md — AI Chip Vibe Lab 컨텍스트

> 이 파일은 Claude Code 또는 호환 에이전트가 본 레포에서 작업할 때 자동으로 로드되는 코스-specific 가이드입니다. 학생/강사가 매 세션마다 같은 컨텍스트를 다시 설명할 필요 없게.

## 1. 코스가 무엇인지

**4주 / 80시간 AI 반도체 설계 실습 코스.** 학생은 매주 5회차(회차당 4시간) 동안 **하나의 가상 NPU를 점진적으로 발전**시키며, 매주 그 위에 새 능력을 쌓습니다.

- Week 1: CPU/GPU 베이스라인 + roofline 모델
- Week 2: TPU systolic array + dataflow 분류
- Week 3: 본인 NPU 설계 + 시뮬레이터
- Week 4: 응용 시나리오 튜닝 + 발표

상세 회차 링크: [CURRICULUM.md](CURRICULUM.md). 환경 셋업: [SETUP.md](SETUP.md).

## 2. 디렉토리 컨벤션

```
week{N}/
├── README.md            # 주차 개요
├── sessions/{N}-{1..5}.md  # 회차별 가이드 (학습 목표 / 산출물 / Part A-D / 평가)
├── lab/                 # 학생이 만드는 코드 (`{회차번호:02}_{이름}.py`)
└── reference/           # 강사용 참조 솔루션 (학생이 막혔을 때 분기 가이드)
```

학생 작업 결과물은 `week{N}/lab/{01..05}_*.py`. 보고서는 `week{N}/docs/{week_report,retrospective-{N}-{M},prompt-log}.md`.

## 3. 학생과 작업할 때 따를 원칙

### 3.1 누적 산출물을 존중

- Week 3 이후 학생은 본인 `NPUConfig`, `MACUnit`, `Memory`, `NPU` 클래스가 있음 — *매번 새로 만들지 말고* 학생의 기존 코드를 사용/수정
- Week 4 응용 튜닝은 3주차 시뮬레이터 위에서 *config 변경* 으로 진행 (시뮬레이터 자체를 다시 짜지 말 것)
- 파괴적 변경(시그니처 바꾸기, 클래스 분할 등)은 *학생과 의논 후*

### 3.2 Reference 솔루션을 즉시 복사하지 말라

`week{N}/reference/` 는 *마지막 안전망*. 학생이 막혔다면:

1. 먼저 함수 *시그니처* 만 보여주기 (예: `def roofline_estimate(n, m, k, peak_gflops, peak_bw_gbps, reuse_factor=1.0): ...`)
2. 학생이 한 번 더 시도하게
3. 그래도 막히면 *첫 번째 검증 기준* 만 보여주기 (예: "result는 `np.allclose(C, A @ B)` True여야 함")
4. 마지막 수단으로 reference 전체

학생 코드와 reference가 *달라도 동일한 검증 기준* 을 만족하면 OK.

### 3.3 프롬프트 로그 5단계 강제

모든 실습은 [`templates/prompt-log.md`](templates/prompt-log.md) 양식대로:

1. **의도 (Intent)** — 무엇을, 왜
2. **프롬프트 (Prompt)** — 입력한 자연어 지시 원문
3. **결과 (Result)** — 만들어진 코드/답변 요약
4. **검증 (Verification)** — 실행 결과, 기대값 비교
5. **재수정 (Revision)** — 추가 지시 또는 직접 수정

학생이 *"바로 코드 만들어줘"* 라고 해도, **의도와 검증 단계를 포함해서** 진행. 단순 코드 dispense는 코스 학습 목표(*왜 이 결정인가*)와 어긋남.

### 3.4 측정 결과의 플랫폼 의존성 인정

reference는 **macOS Apple Silicon (M4 Max)** 에서 검증됨. 학생이 다른 플랫폼이면:

| 플랫폼 | 흔한 차이점 |
| --- | --- |
| Apple Silicon | AMX 매트릭스 코프로세서 → utilization > 100% (1-3 가이드 참조) |
| Apple Silicon | NumPy `axis=0` reduction이 Accelerate streaming으로 빠를 수 있음 (axis=1 ≥ axis=0, 1-2 가이드) |
| Intel/AMD | AVX-512/AVX2 cpuinfo로 정상 검출. 이론 peak 공식 잘 맞음 |
| Linux server | OpenBLAS/MKL 백엔드. utilization 30-70% 정상 |

*측정 절대값* 보다 *자릿수와 경향* 일치 여부 확인.

## 4. 주차별 작업 패턴

### Week 1 — 측정과 모델링

- 도구: numpy + matplotlib
- 작은 N (200~1000) 으로 pure Python 비교
- `time.perf_counter()` + warmup 1회 + 평균 5-10회
- 모든 시간 측정에 `np.allclose()` 검증
- macOS Accelerate spurious warning은 `np.seterr(over='ignore', divide='ignore', invalid='ignore')` 또는 `warnings.filterwarnings('ignore', category=RuntimeWarning)` 으로 억제

### Week 2 — 아키텍처

- 6 loop ordering: NumPy ndarray 인덱싱 사용 (학습 목표는 *접근 패턴*, 측정 절대값 X)
- Systolic array: weight stationary, output 매핑 공식 `t = m + K + n` (M+K+N-1 useful cycles)
- Stationary 비교: 메모리 접근 카운트는 *해석적(analytical)* — 사이클 시뮬 안 해도 OK

### Week 3 — NPU 설계

- `NPUConfig` dataclass: name, defining_feature, dtype, dtype_bytes, pe_array_rows/cols, dataflow, clock_ghz, sram_kb, dram_bw_gbps, target_workload
- `MACUnit(input_dtype, weight_dtype, accum_dtype)` — INT8/INT8/INT8 → 오버플로우 (의도된 실패) 시연 후 INT32 누적으로 수정
- `NPU.run(A, B)` 시그니처: `RunResult(C, cycles, energy_pj, dram_read_bytes, dram_write_bytes, pe_utilization)` 반환
- 4 unit tests 필수: 정확 fit (`pe_util≈1.0`) / 큰 multiple / 작은 (`pe_util<1.0`) / non-square

### Week 4 — 최적화

- DSE: `itertools.product` + `copy.deepcopy(base_cfg)` 로 config sweep
- Pareto: smaller-is-better 가정 (latency, energy 모두 낮을수록 좋음)
- 응용별 우선 metric 통일하지 말 것: 자율주행=*frame ms*, 챗봇=*tokens/sec*, 영상=*TOPS/W*
- *Specialization* vs *Scaling* 구분: 회귀 없으면 scaling, 회귀 있으면 specialization

## 5. 학생 패턴별 대응

| 학생 요청/상태 | 대응 |
| --- | --- |
| *"일단 동작하면 돼"* | 검증 단계 강제 — `assert np.allclose(...)`, 합리적 자릿수 출력 |
| *"좀 더 단순하게"* | 어느 부분이 단순화인지 묻기 (변수명? 알고리즘? 단계 수?) |
| *"reference 보여줘"* | 시그니처/첫 검증만 → 학생이 재시도 → 안 되면 단계별 |
| *"내 결과가 가이드와 달라"* | 플랫폼 차이 가능성 먼저 (4번 표) 확인 |
| *"피어 리뷰 내가 대신 써줘"* | 거절 — 본인 분석이 평가 대상 |
| 학생이 numpy 인덱싱 루프로 cache 효과 측정하려 함 | Python overhead가 cache miss 비용 압도 → pointer chasing 권장 (1-2 가이드) |
| 학생이 INT8 입력에 INT8 누적 사용 | 의도된 실패 시연 (학습 포인트) → 그 후 INT32 누적으로 수정 |

## 6. 산출물 자가 점검 체크리스트 (회차 종료 시)

- [ ] `week{N}/lab/{회차}_*.py` 가 단독 실행되는가
- [ ] 결과 검증 코드(`assert` 또는 print + 기대값) 가 안에 있는가
- [ ] 프롬프트 로그 5단계 모두 작성했는가 (`week{N}/docs/prompt-log.md`)
- [ ] 회고 1줄 이상 (`docs/retrospective-{N}-{M}.md`)
- [ ] 누적 산출물(주차 보고서)이 이전 회차와 일관성 있는가

## 7. 자주 쓰는 명령

```bash
# 환경 활성화 (모든 회차 공통)
source .venv/bin/activate

# 본인 lab 코드 실행
cd week{N}/lab && python {회차}_*.py

# Reference 비교 (강사 또는 막혔을 때)
cd week{N}/reference && python {회차}_*.py

# 모든 reference 한 번에 검증 (강사용)
for w in week1 week2 week3 week4; do
    cd "$w/reference" && for f in 0*.py; do echo "=== $w/$f ===" && python "$f"; done && cd ../..
done
```

## 8. 핵심 메시지 (4주를 통한 학습 목표)

학생이 4주 끝에 본인 말로 설명할 수 있어야 할 것:

1. *"peak ≠ measured"* — utilization, BW, dataflow 셋이 결정
2. *"workload 별로 winner가 다름"* — 한 칩이 모든 응용에 최선이 아님
3. *"defining feature → 수치 우위"* 의 번역 (성공/실패 모두 학습)
4. *"no free lunch"* — 모든 설계 변경은 trade-off
5. *"scaling vs specialization"* — 모두 좋아진 건 단순 scaling, 특정 응용만 개선되고 다른 응용은 회귀하면 specialization

이 다섯 가지가 모든 회차의 *암묵적 평가 기준*입니다.
