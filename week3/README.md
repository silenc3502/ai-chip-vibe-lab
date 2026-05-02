# Week 3 — AI 반도체 설계 및 시뮬레이션

## 학습 목표
스스로 NPU 아키텍처를 설계하고 시뮬레이션을 통해 성능을 평가한다.

## 누적 산출물 (이번 주에 추가되는 것)
**나만의 NPU + 성능 모델**
- `lab/my_npu.py` — 학생이 설계한 NPU 시뮬레이터
- `lab/perf_model.py` — Roofline / MAC 활용률 / 메모리 병목 분석기
- 시뮬레이션 로그 + 결과 보고서

## 회차

### 3-1. NPU 구조 설계
- 블록 다이어그램(PE 어레이, 메모리, 컨트롤러, I/O)을 바이브 코딩으로 도출
- 설계 의도 기록

### 3-2. MAC & 메모리
- MAC 유닛 동작 모델
- 메모리 계층 (SRAM, DRAM) 접근 비용 모델

### 3-3. 시뮬레이션 환경 통합
- Week 1, 2 산출물과 통합한 성능 모델 v2

### 3-4. 연산량 vs 시간
- Arithmetic Intensity, Roofline 모델 도입
- 시뮬레이션 코드 + 로그 분석

### 3-5. 병목 분석
- Memory-bound vs Compute-bound 판별
- 만든 구조를 수치로 평가, 한계점 파악

## 평가 기준
- [ ] NPU 시뮬레이터가 MatMul / Conv 한 종류 이상 처리
- [ ] Roofline 그래프 1장
- [ ] 병목 분석 결과 (메모리 vs 컴퓨트 어느 쪽인가, 근거 수치)
- [ ] 시뮬레이션 로그 (`docs/sim-log.md`)
- [ ] 회차별 프롬프트 로그

## 디렉토리 구조 (예정)
```
week3/
├── README.md
├── lab/
├── reference/
└── docs/
```
