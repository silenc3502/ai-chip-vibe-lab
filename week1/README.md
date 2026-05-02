# Week 1 — AI 반도체 기초

## 학습 목표
CPU, GPU, NPU 등 컴퓨터 구조와 AI 반도체의 개념·특징을 파악하고, 바이브 코딩으로 성능 예측 환경을 구축한다.

## 누적 산출물 (이번 주에 추가되는 것)
**CPU/GPU 베이스라인 시뮬레이터 (Python)**
- `lab/matmul_baseline.py` — NumPy MatMul 측정
- `lab/gpu_model.py` — GPU 동작 모델 (개념적 시뮬레이션)
- 비교 결과 그래프 1장

## 회차

### [1-1. 환경 구축 + 첫 바이브 코딩](sessions/1-1.md)
- 터미널 / 에이전트 / Python 환경 세팅
- 레포 클론, 첫 commit
- 첫 실습: for-loop vs NumPy 행렬곱 시간 비교

### [1-2. CPU 구조 이해 — 메모리 계층과 캐시 효과](sessions/1-2.md)
- ALU, Register, Cache, 메모리 계층
- 실험 1: working set 크기별 접근 시간 (L1/L2/L3 경계 관찰)
- 실험 2: row-major vs column-major 접근 (1-1 가설 검증)

### [1-3. SIMD / 병렬 처리 — 700배 차이를 분해하기](sessions/1-3.md)
- SIMD lane 폭, 이론적 peak GFLOPS 계산
- 실험 1: 이론적 peak vs 측정 NumPy 활용률
- 실험 2: (Python list / NumPy + 루프 / NumPy 벡터화) 3-way 비교

### [1-4. 행렬 연산 시뮬레이션 — Roofline 모델로 CPU vs GPU 예측](sessions/1-4.md)
- Roofline 이론, Arithmetic Intensity, compute-bound vs memory-bound
- 실험 1: CPU roofline 모델로 1-1 측정값 검증
- 실험 2: 같은 모델에 GPU 파라미터를 넣어 speedup 예측 (RTX 4090, H100, M2 GPU)

### [1-5. CPU / GPU / NPU 비교 + Week 1 마무리](sessions/1-5.md)
- NPU가 CPU/GPU와 다른 4가지 (정밀도, 특화 패턴, 데이터 이동, 고정 dataflow)
- 1-4 roofline 모델에 NPU 파라미터(dtype, precision multiplier) 추가
- Week 1 누적 산출물 v1 정리 + 그룹 공유

## 평가 기준
- [ ] 베이스라인 시뮬레이터가 동작하고 합리적 수치를 출력
- [ ] 비교 그래프 1장 (CPU vs GPU 처리 시간 또는 GFLOPs)
- [ ] 회차별 프롬프트 로그 (`docs/prompt-log.md` 또는 별도 파일)
- [ ] 짧은 회고 (`docs/retrospective.md`) — 무엇이 쉬웠고 어려웠는가

## 디렉토리 구조 (예정)
```
week1/
├── README.md          # 이 파일
├── lab/               # 학생 실습 코드
├── reference/         # 강사 참조 솔루션 (수업 후 공개)
└── docs/              # 프롬프트 로그, 회고, 보고서
```
