# SETUP — 실습 환경 구축

이 문서는 코스 시작 전(또는 1-1 회차 Part A에서) 한 번 따라오면 됩니다. 4주 동안 동일한 환경을 사용합니다.

---

## 1. 운영체제

다음 중 하나:

- **Linux** — Ubuntu 22.04+ 권장
- **macOS** — Monterey(12) 이상
- **Windows** — WSL2 + Ubuntu 22.04 (네이티브 PowerShell은 권장하지 않음)

모든 회차는 **터미널 기반**입니다. GUI IDE(VS Code, JetBrains 등)는 보조 도구로만 사용합니다.

---

## 2. Python 3.11+

```bash
python3 --version    # 3.11.x 이상이어야 함
```

설치/업그레이드:
- macOS: `brew install python@3.12`
- Ubuntu: `sudo apt install python3.12 python3.12-venv`
- 또는 [pyenv](https://github.com/pyenv/pyenv)로 버전 관리

---

## 3. 가상환경 + 패키지

레포 루트에서 다음을 실행합니다.

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows WSL/Linux/macOS 동일
pip install --upgrade pip
pip install numpy matplotlib py-cpuinfo cocotb
```

- `numpy`, `matplotlib` — Week 1-4 전반 사용
- `py-cpuinfo` — Week 1-3 (CPU SIMD ISA 검출)
- `cocotb` — Week 3-2 부터 Verilog 검증에 사용

회차마다 추가 패키지가 필요하면 해당 회차 README에 명시합니다.

---

## 4. Git

```bash
git --version    # 2.30+ 권장
```

코스 진행 방식 (강사 안내에 따름):
- 학생 본인 fork에서 작업, 또는
- 공용 레포의 `student/<이름>` 브랜치에서 작업

본인 commit에는 학번/이름을 식별 가능한 형태로 남겨주세요.

---

## 5. 바이브 코딩 에이전트

이 코스의 **핵심 도구**입니다. 강사가 1주차 시작 전 사용할 에이전트를 공지합니다.

권장:
- **Claude Code** — Anthropic 공식 CLI, 터미널 기반, 본 코스의 표준
- 대안: Cursor, Aider, Codex CLI 등

설치 확인:

```bash
# Claude Code 예시
claude --version
```

> ⚠️ 모든 학생이 동일 에이전트를 사용해야 평가 기준이 일관됩니다. 공지된 도구를 사용하세요.

---

## 6. RTL 도구 (Week 3-2 부터 필요)

Week 3-2 회차에서 *Verilog MAC 모듈 + cocotb 테스트벤치* 를 작성합니다. 미리 설치해 두면 회차 시작이 매끄럽습니다.

### 6.1 Icarus Verilog (오픈소스 Verilog 시뮬레이터)

```bash
# macOS
brew install icarus-verilog

# Ubuntu/WSL
sudo apt install iverilog
```

설치 확인:
```bash
iverilog -V    # 11.0 이상 권장
```

### 6.2 GTKWave (waveform 뷰어)

```bash
# macOS
brew install --cask gtkwave

# Ubuntu/WSL
sudo apt install gtkwave
```

설치 확인:
```bash
gtkwave --version    # 3.3.x 이상
```

### 6.3 cocotb (Python testbench, §3 에서 이미 설치)

```bash
python3 -c "import cocotb; print(cocotb.__version__)"   # 1.9 이상 권장
```

> 사전 학습 권장: [`templates/verilog-primer.md`](templates/verilog-primer.md) — Week 3-2 직전에 15-20분 정도 읽고 들어오면 학습 곡선이 완만해집니다.

---

## 7. 동작 확인

다음 명령이 모두 성공하면 준비 완료입니다.

```bash
python3 --version                              # 3.11+
python3 -c "import numpy; print(numpy.__version__)"
python3 -c "import matplotlib; print(matplotlib.__version__)"
python3 -c "import cocotb; print(cocotb.__version__)"
git --version
claude --version    # 또는 강사가 지정한 에이전트
iverilog -V | head -1                          # Week 3-2 부터
gtkwave --version | head -1                    # Week 3-2 부터
```

문제 발생 시 1-1 회차 가이드의 *흔한 막힘 포인트*를 먼저 확인하세요.
