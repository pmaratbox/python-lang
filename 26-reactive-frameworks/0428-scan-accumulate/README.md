# 0428 — Scan (Running Fold)

Use the library's scan operator to emit the running sum of 1, 2, 3, 4. Uses RxPY's `ops.scan` with seed 0 and addition; RxPY does not emit the seed, so no drop is needed.

## Run

    python3 main.py
