# 0656 — Exponential backoff

Uses **tenacity** with an exponential backoff wait strategy
(`wait_exponential(multiplier=0)` for zero delay). A shared counter scripts the
failures: the operation raises three times and then succeeds on the fourth
attempt. tenacity actually drives the retries, and the printed total attempt
count is `4`.

## Run

    python3 main.py
