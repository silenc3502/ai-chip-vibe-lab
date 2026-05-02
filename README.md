# AI Chip Vibe Lab

리눅스 터미널 환경에서 **바이브 코딩(자연어 지시)**으로 AI 반도체를 설계·시뮬레이션·최적화하는 4주 / 80시간 실습 과정.

## 코스 구조

학생은 4주 동안 **하나의 가상 NPU**를 점진적으로 발전시키며, 매주 그 위에 새로운 능력을 쌓습니다.

| 주차 | 주제 | 이번 주에 추가되는 것 | 주요 산출물 |
| --- | --- | --- | --- |
| [Week 1](week1/) | AI 반도체 기초 | CPU/GPU 베이스라인 시뮬레이터 | for-loop vs NumPy, roofline, 5-hardware 비교 |
| [Week 2](week2/) | 아키텍처 분석 | TPU systolic array dataflow 모델 | 6 ordering 분류, 4×4 systolic 시뮬, 칩 분석 보고서 |
| [Week 3](week3/) | 설계 & 시뮬레이션 | 나만의 NPU + 성능 모델 | NPUConfig, MAC/메모리 모델, 통합 시뮬레이터, 병목 분석 |
| [Week 4](week4/) | 최적화 & 응용 | 응용 시나리오 튜닝 + 발표 | DSE Pareto, batching curve, 응용별 specialization |

## 교육 대상

고급과정 수료자 또는 그에 상응하는 역량을 갖춘 자.

## 핵심 도구

- 리눅스 터미널 (또는 macOS terminal / WSL)
- 바이브 코딩 에이전트 (Claude Code, Cursor 등)
- Python 3.11+ (NumPy, matplotlib, py-cpuinfo)
- Git

## 학생 시작하기

1. [SETUP.md](SETUP.md) — 환경 구축 (Python venv, git, 바이브 코딩 에이전트)
2. [Week 1-1](week1/sessions/1-1.md) — 첫 회차 가이드 부터
3. [`templates/prompt-log.md`](templates/prompt-log.md) — 모든 실습에 첨부할 5단계 프롬프트 로그 양식
4. [CLAUDE.md](CLAUDE.md) — 바이브 코딩 에이전트가 자동 로드하는 코스 컨텍스트 (수정 불필요, 참고용)

## 강사 시작하기

각 주차에 강사용 **참조 솔루션**(`reference/`)이 있습니다. 학생이 막혔을 때 *전체 파일을 보여주지 말고* 단계별로 분기시키는 가이드 포함.

| 주차 | 참조 솔루션 |
| --- | --- |
| Week 1 | [week1/reference/](week1/reference/) — 5개 .py + 2개 PNG |
| Week 2 | [week2/reference/](week2/reference/) — 4개 .py + 1개 PNG (2-5는 분석 회차) |
| Week 3 | [week3/reference/](week3/reference/) — 5개 .py + 1개 PNG |
| Week 4 | [week4/reference/](week4/reference/) — 4개 .py + 3개 PNG (4-5는 발표 회차) |

전체 reference는 macOS Apple Silicon (M4 Max)에서 검증되었으며, *플랫폼 의존성*(예: Apple AMX 매트릭스 코프로세서로 인한 utilization > 100% 현상)은 각 세션 가이드의 *흔한 막힘 포인트*에 명시되어 있습니다.

## 평가 원칙

모든 산출물은 다음 두 축으로 평가:

1. **결과물의 기술적 정합성** — 시뮬레이터/모델이 실제로 동작하고 수치가 합리적인가
2. **프롬프트 로그의 품질** — [`templates/prompt-log.md`](templates/prompt-log.md) 5단계(의도 → 프롬프트 → 결과 → 검증 → 재수정)를 충실히 따랐는가

주차별 평가 비중은 [CURRICULUM.md](CURRICULUM.md) 참고.

## 문서

- [CURRICULUM.md](CURRICULUM.md) — 4주 × 5회차 상세 일정 + 회차 링크
- [SETUP.md](SETUP.md) — 실습 환경 구축 가이드
- [CLAUDE.md](CLAUDE.md) — 에이전트 자동 컨텍스트 (학생/강사가 매번 설명 안 해도 됨)
- [templates/](templates/) — 프롬프트 로그 등 공용 템플릿

## 디렉토리 구조

```
ai-chip-vibe-lab/
├── README.md, CURRICULUM.md, SETUP.md
├── templates/prompt-log.md
├── week{1,2,3,4}/
│   ├── README.md              # 주차 개요, 회차 링크
│   ├── sessions/{N}-{1..5}.md # 회차별 가이드 (학습 목표 / 산출물 / Part A-D / 평가)
│   ├── lab/                   # 학생이 만드는 코드
│   └── reference/             # 강사용 참조 솔루션
└── .venv/                     # 가상환경 (SETUP.md 참고)
```
