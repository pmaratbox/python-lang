# 0108 — Parallel Tasks Combined

Run two independent tasks that produce 10 and 20 concurrently, then combine (sum) their results into `30`. Two `Future` objects from a `ThreadPoolExecutor` run concurrently and `.result()` joins them.

## Run

    python3 main.py
