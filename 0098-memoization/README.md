# 0098 — Memoization

Compute `fibonacci(10)` recursively with memoization (caching each result so it is computed once) and print it: `55`. A dict caches each computed `fib(n)` so repeated subproblems are returned instantly (`functools.lru_cache` automates this).

## Run

    python3 main.py
