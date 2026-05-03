# 02_mac_verilog — Verilog MAC + cocotb 참조 솔루션 (3-2)

**선수**: [`templates/verilog-primer.md`](../../../templates/verilog-primer.md) 한 번 읽고 들어옴.

## 파일

| 파일 | 역할 |
| --- | --- |
| `mac.v` | signed INT8 × INT8 → INT32 누적 MAC (40줄) |
| `test_mac.py` | cocotb testbench, 4 테스트 (basic / signed / no-overflow / Python cross-check) |
| `Makefile` | icarus 시뮬 + cocotb 표준 |
| `dump.vcd` | (실행 후 생성) waveform — `gtkwave dump.vcd` 로 확인 |

## 실행

```bash
source ../../../.venv/bin/activate
make           # 4개 테스트 실행 (TESTS=4 PASS=4 기대)
gtkwave dump.vcd &   # waveform 시각화 (선택)
```

## 강사 분기 가이드 — 학생 막힘 단계별

| 학생 막힘 | 보여줄 부분 |
| --- | --- |
| `module` 골격을 못 짬 | `mac.v` 의 port 선언만 (`module mac (...);` 부분) |
| `always @(posedge clk)` 패턴 모름 | primer §2 다시 + 1-2 줄 시연 |
| 누적 비트 폭 결정 못 함 | INT8×INT8=INT16, 1000회 누적 → INT32 권장 — 직접 계산하게 |
| cocotb syntax 막힘 | `test_basic` 의 reset + feed_pair 패턴만 |
| Python ↔ RTL 결과 다름 | signed/unsigned 캐스팅 점검 (둘 다 signed 인지) |

## 핵심 학습 포인트

1. **Width discipline** — INT8 입력은 자연스럽게 16-bit 곱 결과. 32-bit 누적은 안전.
2. **Signed 키워드** — `wire signed [7:0]` 명시. unsigned 면 음수가 큰 양수처럼 처리됨.
3. **Python ↔ Verilog cross-check** — *같은 알고리즘의 두 추상화 레벨* 이 같은 결과를 내는 경험. 이게 본 회차의 핵심 학습 산출물.

## 검증 결과 (M4 Max, cocotb 2.0.1, icarus 13.0)

```
TESTS=4 PASS=4 FAIL=0
test_basic                    PASS
test_signed                   PASS
test_no_overflow_with_int32   PASS  (1000회 누적, INT32 안전)
test_cross_check_python       PASS  (RTL=2413, Python=2413, 100 pairs)
```
