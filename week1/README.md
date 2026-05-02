# Week 1 — AI 반도체 기초

## 학습 목표
CPU, GPU, NPU 등 컴퓨터 구조와 AI 반도체의 개념·특징을 파악하고, 바이브 코딩으로 성능 예측 환경을 구축한다.

## 누적 산출물 (이번 주에 추가되는 것)
**CPU/GPU 베이스라인 시뮬레이터 (Python)**
- `lab/matmul_baseline.py` — NumPy MatMul 측정
- `lab/gpu_model.py` — GPU 동작 모델 (개념적 시뮬레이션)
- 비교 결과 그래프 1장

## 회차

### 1-1. 환경 구축 + 첫 바이브 코딩
- 터미널 / 에이전트 / Python 환경 세팅
- 레포 클론, 첫 commit
- "Hello, AI chip" 실습 — 바이브 코딩으로 5줄짜리 스크립트 만들기

### 1-2. CPU 구조 이해
- ALU, Register, Cache, 메모리 계층
- Python으로 단순 연산 시간 측정 (캐시 효과 관찰)

### 1-3. SIMD / 병렬 처리
- 벡터화 개념, 루프 vs NumPy 비교
- CPU vs GPU 근본 차이 토의

### 1-4. 행렬 연산 시뮬레이션
- NumPy MatMul 측정
- GPU 모델로 동일 연산 시뮬레이션, 비교

### 1-5. CPU / GPU / NPU 비교
- 왜 AI는 GPU에서 NPU로 가는가
- Week 1 산출물 v1 정리, 회고

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
