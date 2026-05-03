# Verilog Primer — 1 Page Reference

> Week 3-2 회차 *전*에 15-20분 정도 읽고 들어오면 학습 곡선이 매끄럽습니다. 본 코스에서 쓰는 패턴만 다룹니다 — 완전한 언어 스펙이 아님.

## 1. 한 모듈의 골격

```verilog
module mac (
    input  wire        clk,            // 클럭 (입력)
    input  wire        rst,            // 동기 리셋 (입력)
    input  wire [7:0]  in_data,        // 8-bit 부호없는 입력
    input  wire [7:0]  weight,         // 8-bit 가중치
    output reg  [31:0] acc             // 32-bit 누적 (출력, 레지스터)
);
    // 동기 회로: clk 의 rising edge 마다 동작
    always @(posedge clk) begin
        if (rst)
            acc <= 32'd0;               // 리셋 시 0
        else
            acc <= acc + (in_data * weight);  // 매 cycle 누적
    end
endmodule
```

핵심 포인트:
- `module ... endmodule` — 한 단위 회로
- `input/output` 으로 외부 인터페이스 선언
- `[N-1:0]` — N-bit 폭 (예: `[7:0]` = 8 bit)
- `wire` — 조합 회로 신호 (combinational), `reg` — 레지스터 (sequential)
- 출력에 *값을 저장*하면 `output reg`, 그냥 *연결*하면 `output wire`

## 2. always 블록의 두 종류

```verilog
// (a) 동기 회로: clk 마다 업데이트, non-blocking 할당 <=
always @(posedge clk) begin
    acc <= acc + 1;       // 다음 clock edge 에 반영
end

// (b) 조합 회로: 입력 변화 시 즉시 업데이트, blocking 할당 =
always @(*) begin
    out = a + b;          // 즉시 반영
end
```

**규칙**:
- `always @(posedge clk)` 안에서는 `<=` (non-blocking)
- `always @(*)` 또는 일반 always 안에서는 `=` (blocking)
- 섞으면 latch 또는 race condition 발생 — 흔한 함정

## 3. 비트 폭 명시 — 가장 흔한 오류

```verilog
// ❌ 잘못: 8-bit 결과에 누적하면 오버플로우
reg [7:0] bad_acc;
always @(posedge clk) bad_acc <= bad_acc + in_data * weight;
// in_data*weight = 16 bit. bad_acc 가 8 bit 라 손실.

// ✅ 정답: 누적은 더 큰 폭으로
reg [31:0] good_acc;
always @(posedge clk) good_acc <= good_acc + (in_data * weight);
// in_data*weight 자동으로 16 bit, good_acc 가 32 bit 라 안전
```

INT8 × INT8 = INT16. INT16 을 N 번 누적 → 최대 INT16 + log2(N) bits 필요. **본 코스에서는 INT8 입력 누적은 INT32 로 통일**.

## 4. 부호 있는 (signed) 곱셈

```verilog
input wire signed [7:0] in_data;          // -128 ~ 127
input wire signed [7:0] weight;
output reg  signed [31:0] acc;

always @(posedge clk) acc <= acc + (in_data * weight);
```

`signed` 키워드 없으면 unsigned 로 해석되어 음수가 큰 양수처럼 처리됨. **NPU 에서는 signed 사용 권장**.

## 5. Testbench 측 (cocotb 에서 자주 쓰는)

```verilog
// dump waveform 위해 dut 모듈 끝에 추가 (선택)
initial begin
    $dumpfile("dump.vcd");
    $dumpvars(0, mac);
end
```

cocotb 가 호출하면 `dump.vcd` 생성 → GTKWave 로 열어 신호 확인.

## 6. cocotb Python 측 — 자주 쓰는 패턴

```python
import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge

@cocotb.test()
async def test_basic(dut):
    # 1. clock 시작 (10ns 주기 = 100 MHz)
    cocotb.start_soon(Clock(dut.clk, 10, "ns").start())

    # 2. 리셋
    dut.rst.value = 1
    await RisingEdge(dut.clk)
    dut.rst.value = 0

    # 3. 입력 인가
    dut.in_data.value = 5
    dut.weight.value = 3
    await RisingEdge(dut.clk)

    # 4. 결과 확인
    assert int(dut.acc.value) == 15
```

## 7. 컴파일/실행 표준 Makefile

```makefile
SIM ?= icarus
TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES = mac.v
TOPLEVEL = mac           # 시뮬할 top 모듈명
MODULE = test_mac        # cocotb 테스트 파일명 (.py 빼고)

include $(shell cocotb-config --makefiles)/Makefile.sim
```

실행:
```bash
make            # 시뮬 실행
make WAVES=1    # waveform 추가 생성 (도구별)
gtkwave dump.vcd  # waveform 확인
```

## 8. 흔한 함정

| 증상 | 원인 | 해결 |
| --- | --- | --- |
| `unknown module` | VERILOG_SOURCES 에 .v 파일 누락 | Makefile 점검 |
| `module 'mac' not found` | TOPLEVEL 이름이 module 이름과 안 맞음 | 일치시킴 |
| 누적 결과가 작거나 wrap-around | `reg [N:0]` 폭이 작음 | INT32 또는 더 크게 |
| `assert dut.acc.value == 15` 실패 | 비교 시 `int(...)` 누락 — `LogicArray` 객체 비교 | `int(dut.acc.value)` 사용 |
| `dut.signal.value = -3` 후 부호 깨짐 | unsigned 모듈에 음수 입력 | signed 명시 또는 2's complement 변환 |
| Latch warning | `always @(*)` 에서 모든 분기에 값 할당 안 함 | `else` 또는 default 추가 |

## 9. 외부 자료 (더 깊이)

- [HDLBits](https://hdlbits.01xz.net/) — 인터랙티브 Verilog 문제 (영어)
- [ASIC World — Verilog](https://www.asic-world.com/verilog/index.html) — 표준 reference (영어)
- [Asynchronous Logic in Verilog (Korean)](https://wikidocs.net/240020) — 한국어 입문서

## 10. 본 코스에서 *안* 쓰는 것

- `initial` 블록 (testbench 외) — 합성 안 됨
- `for` 루프 (제한적 사용 가능하지만 본 코스 회차에서는 회피)
- SystemVerilog 고급 기능 (`interface`, `package`, `logic` 타입) — 일부 시뮬레이터 미지원
- formal verification — 별도 도구 필요
