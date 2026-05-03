# Week 3 — AI 반도체 설계 및 시뮬레이션

## 학습 목표
스스로 NPU 아키텍처를 설계하고 시뮬레이션을 통해 성능을 평가한다.

## 누적 산출물 (이번 주에 추가되는 것)
**나만의 NPU + 성능 모델 + RTL anchor**
- `lab/01_npu_config.py` ~ `05_npu_optimize.py` — Python 시뮬레이터 (Config / MAC / Memory / NPU / Optimization)
- `lab/02_mac_verilog/{mac.v, test_mac.py, Makefile}` — **Verilog MAC + cocotb 검증** (3-2)
- `lab/04_cycle_compare/{Makefile, test_cycle_compare.py}` — **RTL ↔ Python 사이클 비교** (3-4, 3-2 의 mac.v 재사용)
- 시뮬레이션 로그 + 결과 보고서

## 회차

### [3-1. NPU 구조 설계 — 베팅을 정하기](sessions/3-1.md)
- Defining feature, dtype, dataflow, PE array 모양 결정
- 블록 다이어그램 + NPUConfig dataclass

### [3-2. MAC 유닛 — Python + Verilog 두 추상화 레벨](sessions/3-2.md)
- Python `MACUnit` 클래스 (input/weight/accumulator dtype 분리)
- **Verilog `mac.v` + cocotb testbench** (signed INT8 × INT8 → INT32)
- INT8 누적 오버플로우 *의도된 실패* 실험
- Python ↔ Verilog 결과 cross-check

### [3-3. 시뮬레이션 환경 구축 — NPU 통합 시뮬레이터](sessions/3-3.md)
- 3-1 config + 3-2 부품 + 2-2 systolic을 합쳐 `NPU.run(workload)`
- 4개 단위 테스트 (정확/큰/작은/non-square 워크로드)

### [3-4. 연산량 vs 시간 — Roofline + RTL 사이클 검증](sessions/3-4.md)
- 5개 표준 AI 워크로드 측정
- Roofline 차트 + Week 2 칩 카탈로그와 cross-comparison
- **3-2 의 `mac.v` 재사용해서 1024 dot product RTL 사이클 측정**
- Python 모델 cycle 예측 vs RTL 실측 비교
- *Defining feature → 수치 우위* 번역 자가 평가

### [3-5. 병목 찾기 + 1회 설계 변경 — Week 3 마무리](sessions/3-5.md)
- 병목 진단 (memory / compute / underutilized)
- 1회 설계 변경 → 재측정 → trade-off 분석
- Week 3 누적 보고서 작성

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
