# 0641 — Put and get

Uses **cachetools.LRUCache** (a strict least-recently-used cache) to store the
value `1` under key `a`, then retrieves it with `get`, which returns the stored
value `1` (and would return the `"miss"` default for an absent key).

## Run

    python3 main.py
