# 0651 — Retries exhausted

Uses **tenacity** (`Retrying` with `stop_after_attempt(3)` and `wait_none()`) to
drive a scripted operation that always raises. The library makes 3 total
attempts (the first call plus 2 retries) with zero delay; once the stop
condition is reached `reraise=True` re-raises the final `ValueError`, which we
catch and report as `failed`.

## Run

    python3 main.py
