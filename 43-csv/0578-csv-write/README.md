# 0578 — Write CSV

Writes two rows (`["name", "age"]` then `["Alice", "30"]`) to CSV with Python's standard-library `csv` module (`csv.writer` over an `io.StringIO` buffer). The writer emits `\r\n` line terminators, so the output is normalized to `\n` and the trailing newline stripped before printing `name,age` / `Alice,30`.

## Run

    python3 main.py
