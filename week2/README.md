# Week 2 — AI 반도체 아키텍처 분석

## 학습 목표
AI 반도체 아키텍처 설계 방법론을 학습하고 최신 사례를 분석한다. 자연어 지시로 가속 원리를 검증할 수 있다.

## 누적 산출물 (이번 주에 추가되는 것)
**TPU 스타일 systolic array dataflow 모델**
- `lab/systolic_array.py` — N×N PE 어레이 시뮬레이션
- `lab/dataflow_compare.py` — Weight / Output / Input stationary 비교
- 아키텍처 분석 보고서 1편

## 회차

### [2-1. MatMul & Dataflow 개념](sessions/2-1.md)
- 6가지 loop ordering MatMul 시간 비교
- Dataflow 개념 — 어떤 데이터가 정지/흐른다
- Output / Input / Weight Stationary 분류

### [2-2. TPU 분석 — Systolic Array 시뮬레이션](sessions/2-2.md)
- Google TPU 역사와 설계 동기
- Systolic array의 사이클 단위 동작
- 4×4 PE 시뮬레이터 작성

### [2-3. Stationary 비교](sessions/2-3.md)
- WS / OS / IS 3종 시뮬레이션
- DRAM read/write, PE move 카운팅
- 워크로드별 winner가 다름을 측정으로 확인

### [2-4. 통합 비교 — Roofline에 TPU 추가](sessions/2-4.md)
- 1-4 모델에 systolic reuse_factor 반영
- 5개 워크로드 × 5개 칩 비교 표
- "이 구조가 왜 빠른가?" 한 줄씩

### [2-5. 아키텍처 분석 보고서](sessions/2-5.md)
- TPU 외 칩 1종 (Tenstorrent / Groq / Cerebras / Graphcore 등)
- Defining architectural feature 식별
- 1-2 page 보고서 + 5분 발표 + 피어 평가

## 평가 기준
- [ ] systolic array 시뮬레이터 동작 및 결과 일관성
- [ ] Stationary 3종 비교 결과 (메모리 접근량, 사이클 수)
- [ ] 아키텍처 분석 보고서 (분량 무관, 그림 포함)
- [ ] 회차별 프롬프트 로그

## 디렉토리 구조 (예정)
```
week2/
├── README.md
├── lab/
├── reference/
└── docs/
```
