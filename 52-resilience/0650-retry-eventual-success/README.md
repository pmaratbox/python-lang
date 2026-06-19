# 0650 — Eventual success

Uses **tenacity** (`Retrying` with `stop_after_attempt` and `wait_none`) to drive
a scripted operation that fails once then succeeds. A shared counter records each
invocation, so after the library retries the failing call exactly once the total
attempt count prints as `2`.

## Run

    python3 main.py
