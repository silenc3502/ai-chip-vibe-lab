# 커리큘럼 상세

총 4주 × 5회차 × 4시간 = **80시간**.

각 회차는 *이론 강의*와 *바이브 코딩 실습*을 결합하며, 회차 종료 시 프롬프트 로그를 누적 저장합니다.

> 표의 회차 번호는 세션 가이드 링크입니다. [SETUP.md](SETUP.md)부터 시작하세요.

---

## [Week 1](week1/README.md) — AI 반도체 기초

**누적 산출물:** CPU/GPU 베이스라인 시뮬레이터 (Python)

| 회차 | 주제 | 강의내용 | 방식 |
| --- | --- | --- | --- |
| [1-1](week1/sessions/1-1.md) | 환경 구축 + 첫 바이브 코딩 | 터미널 / 에이전트 / 레포 세팅, for-loop vs NumPy MatMul | 실습 |
| [1-2](week1/sessions/1-2.md) | CPU 구조 이해 | 메모리 계층 + pointer chasing으로 cache step 관찰 | 이론/실습 |
| [1-3](week1/sessions/1-3.md) | SIMD / 병렬 처리 | 700배 차이를 (캐시 × SIMD × 인터프리터)로 분해 | 이론/실습 |
| [1-4](week1/sessions/1-4.md) | 행렬 연산 시뮬레이션 | Roofline 모델로 CPU 검증 + GPU 예측 | 이론/실습 |
| [1-5](week1/sessions/1-5.md) | CPU / GPU / NPU 비교 | NPU 파라미터 추가, 5-hardware 비교 + Week 1 보고서 | 이론/실습 |

---

## [Week 2](week2/README.md) — AI 반도체 아키텍처 분석

**누적 산출물:** TPU 스타일 systolic array dataflow 모델

| 회차 | 주제 | 강의내용 | 방식 |
| --- | --- | --- | --- |
| [2-1](week2/sessions/2-1.md) | MatMul & Dataflow | 6 loop ordering → 3 stationary 분류 | 이론/실습 |
| [2-2](week2/sessions/2-2.md) | TPU 분석 | 4×4 systolic array cycle-by-cycle 시뮬레이터 | 이론/실습 |
| [2-3](week2/sessions/2-3.md) | Stationary 비교 | WS / OS / IS 메모리 접근 카운팅 | 이론/실습 |
| [2-4](week2/sessions/2-4.md) | 통합 비교 | Roofline에 TPU 추가, 5×5 워크로드 비교 표 | 이론/실습 |
| [2-5](week2/sessions/2-5.md) | 아키텍처 분석 보고서 | 새 칩 1종 분석 + 발표 + 피어 리뷰 | 실습 |

---

## [Week 3](week3/README.md) — AI 반도체 설계 및 시뮬레이션

**누적 산출물:** 나만의 NPU + 성능 모델 (roofline, MAC 활용률, 메모리 병목)

| 회차 | 주제 | 강의내용 | 방식 |
| --- | --- | --- | --- |
| [3-1](week3/sessions/3-1.md) | NPU 구조 설계 | Defining feature 결정, 블록 다이어그램, NPUConfig | 실습 |
| [3-2](week3/sessions/3-2.md) | MAC & 메모리 | MAC 유닛 + 3-tier 메모리 모델링, INT8 오버플로우 실험 | 이론/실습 |
| [3-3](week3/sessions/3-3.md) | 시뮬레이션 통합 | NPU 통합 시뮬레이터 + 4 단위 테스트 | 이론/실습 |
| [3-4](week3/sessions/3-4.md) | 연산량 vs 시간 | 5 워크로드 측정 + roofline + 칩 카탈로그와 cross-comparison | 이론/실습 |
| [3-5](week3/sessions/3-5.md) | 병목 분석 | 병목 식별 + 1회 설계 변경 + Week 3 보고서 | 이론/실습 |

---

## [Week 4](week4/README.md) — AI 반도체 최적화 및 응용 설계

**누적 산출물:** 응용 시나리오 튜닝 결과 + 발표 자료

| 회차 | 주제 | 강의내용 | 방식 |
| --- | --- | --- | --- |
| [4-1](week4/sessions/4-1.md) | 최적화 개념 | Pareto front, 48-config DSE sweep | 이론/실습 |
| [4-2](week4/sessions/4-2.md) | 성능 축 | Latency vs Throughput batching curve, cost 모델 | 이론/실습 |
| [4-3](week4/sessions/4-3.md) | 응용 시나리오 | 자율주행 / 챗봇 / 영상처리 워크로드 분석 | 이론/실습 |
| [4-4](week4/sessions/4-4.md) | 응용 맞춤 튜닝 | 응용에 맞춰 재설계 + specialization 비용 측정 | 이론/실습 |
| [4-5](week4/sessions/4-5.md) | 발표 & 피어 리뷰 | 8-10분 발표, 80시간 코스 회고 | 발표 |

---

## 주차별 평가 비중 (제안)

| 항목 | 비중 |
| --- | --- |
| 누적 산출물 (코드/시뮬레이터) | 50% |
| 프롬프트 로그 품질 | 30% |
| 보고서 / 발표 | 20% |
