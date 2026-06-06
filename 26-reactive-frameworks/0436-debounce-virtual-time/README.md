# 0436 — Debounce (Virtual Time)

Use the library's debounce operator on a virtual/test scheduler to emit a value only after a quiet window. Uses RxPY's `ops.debounce` driven by `TestScheduler` for deterministic virtual time.

## Run

    python3 main.py
