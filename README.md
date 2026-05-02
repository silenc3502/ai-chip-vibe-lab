# AI Chip Vibe Lab

리눅스 터미널 환경에서 **바이브 코딩(자연어 지시)**으로 AI 반도체를 설계·시뮬레이션·최적화하는 4주 / 80시간 실습 과정입니다.

## 누적 산출물 구조

학생은 4주 동안 **하나의 가상 NPU**를 점진적으로 발전시키며, 매주 그 위에 새로운 능력을 쌓습니다.

| 주차 | 주제 | 이번 주에 추가되는 것 |
| --- | --- | --- |
| [Week 1](week1/) | AI 반도체 기초 | CPU/GPU 베이스라인 시뮬레이터 (Python) |
| [Week 2](week2/) | 아키텍처 분석 | TPU 스타일 systolic array dataflow 모델 |
| [Week 3](week3/) | 설계 & 시뮬레이션 | 나만의 NPU + 성능 모델 (roofline, 병목 분석) |
| [Week 4](week4/) | 최적화 & 응용 | 응용 시나리오에 맞춘 튜닝 + 발표 |

## 교육 대상

고급과정 수료자 또는 그에 상응하는 역량을 갖춘 자.

## 핵심 도구

- 리눅스 터미널 (또는 macOS terminal / WSL)
- 바이브 코딩 에이전트 (Claude Code, Cursor 등)
- Python 3.11+ (NumPy, matplotlib)
- Git

## 평가 원칙

모든 산출물은 다음 두 축으로 평가합니다.

1. **결과물의 기술적 정합성** — 시뮬레이터/모델이 실제로 동작하고 수치가 합리적인가
2. **프롬프트 로그의 품질** — [`templates/prompt-log.md`](templates/prompt-log.md) 5단계 (의도 → 프롬프트 → 결과 → 검증 → 재수정) 를 충실히 따랐는가

## 문서

- [CURRICULUM.md](CURRICULUM.md) — 4주 × 5회차 상세 일정
- [templates/](templates/) — 프롬프트 로그 등 공용 템플릿
