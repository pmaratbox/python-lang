# 0653 — Count attempts

Uses **tenacity** (`Retrying` with `stop_after_attempt(5)` and `wait_none()`) to
drive a scripted operation that always raises. A shared counter records each
attempt; after tenacity exhausts the 5 allowed attempts and re-raises, the total
number of attempts made (`5`) is printed.

## Run

    python3 main.py
