# 0380 — Compare-And-Swap Loop

Increment a shared value to 100 using a CAS retry loop from multiple threads, printing `100`. A lock-guarded compare-and-swap retries until the expected value still holds before committing the increment.

## Run

    python3 main.py
