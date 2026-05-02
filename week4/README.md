# Week 4 — AI 반도체 최적화 및 응용 설계

## 학습 목표
응용 분야에 최적화된 구조를 제안하고, 비용·성능 트레이드오프를 이해한다.

## 누적 산출물 (이번 주에 추가되는 것)
**응용 시나리오 튜닝 결과 + 발표 자료**
- `lab/scenario_tuning.py` — 시나리오별 NPU 변형 (자율주행 / 챗봇 / 영상)
- `docs/final_report.md` — 문제 정의 → 구조 → 성능 최적화
- 발표 슬라이드 (선택)

## 회차

### [4-1. 최적화 개념 — Pareto Front + DSE](sessions/4-1.md)
- 48 config sweep, (latency, energy) 평면에 plot
- Pareto front 식별, 본인 base config 위치 평가

### [4-2. 성능 축 — Latency/Throughput, Cost/Performance](sessions/4-2.md)
- Batching curve, knee point 식별
- 다이 면적 + 전력 추정 모델
- Cost 추가한 확장 Pareto

### [4-3. 응용 시나리오 — 자율주행 / 챗봇 / 영상](sessions/4-3.md)
- 3 응용의 워크로드 특성 + 우선 metric
- 본인 NPU에서 3 응용 모두 측정
- 4-4 대상 응용 1개 선택

### [4-4. 응용 맞춤 튜닝 — Specialization 비용 측정](sessions/4-4.md)
- 대상 응용에 맞춰 NPUConfig 재설계
- 다른 응용에서의 회귀 측정 (specialization_efficiency)
- 4-5 발표 슬라이드 5장 초안

### [4-5. 발표 + 피어 리뷰 + 코스 마무리](sessions/4-5.md)
- 8-10분 발표 (문제 → 구조 → 결과)
- 피어 리뷰 1편 이상
- 80시간 코스 회고 (7개 섹션)

## 평가 기준
- [ ] 시나리오 1개에 대한 NPU 튜닝 결과 (변경 전/후 수치)
- [ ] 최종 보고서 (`docs/final_report.md`)
- [ ] 발표 수행
- [ ] 피어 리뷰 작성 (다른 학생 1명 이상)
- [ ] 회차별 프롬프트 로그

## 디렉토리 구조 (예정)
```
week4/
├── README.md
├── lab/
├── reference/
└── docs/
```
