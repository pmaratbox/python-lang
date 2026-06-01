# 0022 — Concurrency

Start two tasks that produce `1` and `2`, let them run concurrently, then join their results and print `sum: 3`. A `ThreadPoolExecutor` runs each `submit` on a worker thread, and `.result()` blocks for the value. Because of the Global Interpreter Lock, CPU-bound Python threads don't run in parallel — they shine for I/O — whereas `ProcessPoolExecutor` gives true parallelism.

## Run

    python3 main.py
