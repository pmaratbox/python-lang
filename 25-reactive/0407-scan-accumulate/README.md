# 0407 — Scan (Running Fold)

Implement a scan operator that emits the running accumulation; produce the running sums of 1, 2, 3, 4. A closure-captured dict holds the seeded state so each pushed value updates and re-emits it.

## Run

    python3 main.py
