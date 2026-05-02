# Week 2 — AI 반도체 아키텍처 분석

## 학습 목표
AI 반도체 아키텍처 설계 방법론을 학습하고 최신 사례를 분석한다. 자연어 지시로 가속 원리를 검증할 수 있다.

## 누적 산출물 (이번 주에 추가되는 것)
**TPU 스타일 systolic array dataflow 모델**
- `lab/systolic_array.py` — N×N PE 어레이 시뮬레이션
- `lab/dataflow_compare.py` — Weight / Output / Input stationary 비교
- 아키텍처 분석 보고서 1편

## 회차

### 2-1. MatMul & Dataflow 개념
- 행렬곱 분해 (inner / outer / Gustavson product)
- Dataflow 개념과 의미

### 2-2. TPU 분석
- Google TPU v1~v4 개념 수준 분석
- AI 반도체 아키텍처 카탈로그 (TPU, Tenstorrent, Groq, Graphcore 등)

### 2-3. Stationary 비교
- Weight stationary vs Output stationary vs Input stationary
- 같은 MatMul을 세 방식으로 시뮬레이션, 메모리 접근량 비교

### 2-4. 통합 비교
- CPU vs GPU vs NPU vs TPU
- "이 구조가 왜 빠른가?" — 각 구조의 결정적 차이를 한 문장으로

### 2-5. 아키텍처 분석 보고서
- 선택한 칩 1종에 대한 구조 분석 (블록 다이어그램, 강점/약점, 적합한 워크로드)
- 발표 또는 제출

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
