# 0649 — Succeeds first try

Uses **tenacity.Retrying** (a real retry/resilience library) to wrap an
operation that succeeds on its first call. A shared counter records each
attempt; because the operation never raises, the library invokes it exactly
once and the printed attempt count is `1` (no retry needed).

## Run

    python3 main.py
