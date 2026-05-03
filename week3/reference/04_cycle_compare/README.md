# 04_cycle_compare — Python 모델 ↔ RTL 사이클 비교 (3-4)

**선수**: 3-2 회차 완료 (학생이 본인 `mac.v` 작성). 이 회차는 *그 MAC 을 재사용*해 1024-element dot product 를 RTL 에서 실측합니다.

## 파일

| 파일 | 역할 |
| --- | --- |
| `Makefile` | `VERILOG_SOURCES = ../02_mac_verilog/mac.v` 로 3-2 의 MAC 재사용 |
| `test_cycle_compare.py` | K=1024 dot product, RTL 사이클 측정 + Python NPU 예측 비교 |
| `dump.vcd` | (실행 후) waveform |

## 실행

```bash
source ../../../.venv/bin/activate
make
```

## 검증된 출력 (M4 Max)

```
RTL    :   1025 cycles, acc = -26961
Python :   2025 cycles (predicted), acc = -26961
NumPy ground truth                  acc = -26961
Cycle ratio (Python_predicted / RTL_actual): 1.98×
```

## 핵심 학습 포인트

**값은 동일, 사이클은 다름.** 무엇을 의미하는가:

1. **추상화 레벨이 달라도 결과는 같다** — RTL 과 Python 모두 NumPy ground truth 와 일치 (-26961). *알고리즘은 같다, 표현이 다를 뿐*.

2. **사이클 차이는 *모델의 가정*에서 옴** — Python NPU 모델은 1 μs (= 1000 cycle) 의 *dispatch overhead* 를 가정. 실제 RTL 은 reset 후 바로 시작 → overhead 거의 없음.
   - RTL pure compute: K=1024 + 1 settle = **1025 cycles**
   - Python prediction: 1000 (overhead) + ~1025 (compute) = **2025 cycles**

3. **이 차이가 *틀린* 게 아니라 *현실적*** — 실제 NPU 시스템에서는 host CPU → NPU 명령 전달, kernel 시작 등에 overhead 있음. 모델이 이걸 *포함* 하면 실 시스템 latency 더 잘 예측.

4. **모델 정교화의 trade-off** — 모델을 RTL 에 정확히 맞추면 (overhead=0) 단일 호출은 잘 맞지만 *시스템 latency* 는 과소평가. 모델에 overhead 두면 *시스템 latency* 는 잘 맞지만 *RTL pure compute* 와는 차이.

## 학생 회고 질문 (3-4 가이드)

- 본인 RTL 측정 사이클은? Python NPU 예측은? 비율은?
- 정답값은 모두 일치하는가? (당연히 그래야 함)
- 1.98× 비율이 *틀림* 인가 *현실 반영* 인가? 본인 응용(자율주행/챗봇/영상)에 어느 쪽이 더 정확할까?

## 강사 분기 가이드

| 학생 막힘 | 보여줄 부분 |
| --- | --- |
| `feed_pair` 하면서 cycle 측정 모름 | `get_sim_time(unit="ns")` 사용 — primer §6 + 이 reference 의 start_ns/end_ns 패턴 |
| Python NPU 의 `pe_array_rows=1` 설정 모름 | `make_reference_config()` 호출 후 `cfg.pe_array_rows = 1` 한 줄만 보여주기 |
| RTL acc 값이 NumPy 와 다름 | signed 캐스팅 점검, `.value.to_signed()` 사용 |
| Python acc 가 -81 또는 작은 값 (overflow) | 03 의 NPU.run 가 INT32 결과 반환하는지 확인 — 본 reference 가 fix 한 부분 |
| 사이클 차이가 클수록 학생 *불안* | 학습 포인트로 명시 — *값은 일치, 사이클은 모델 가정에 따라 다름* |
