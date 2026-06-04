# 0103 — Mutex-Protected Counter

Have multiple threads each increment a shared counter under a mutex so the total is exactly `1000`. A `threading.Lock` used as a context manager guards each increment.

## Run

    python3 main.py
