# 0523 — Difference in days

Uses the `pendulum` library to parse two fixed ISO dates and compute the number of whole days between them via `diff().in_days()`. The dates are fixed (`2026-06-15` and `2026-07-15`), so the result is deterministic and never depends on the current time.

## Run

    python3 main.py
