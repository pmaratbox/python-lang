# 0104 — Atomic Counter

Increment a shared atomic counter from multiple threads 1000 times total without a lock, printing `1000`. CPython's `itertools.count` advances atomically under the GIL, so `next()` needs no explicit lock.

## Run

    python3 main.py
