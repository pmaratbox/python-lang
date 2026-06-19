# 0642 — Cache miss

Uses `cachetools.LRUCache`, Python's strict-LRU cache. Looking up the absent key `x` in an empty cache via `get(key, default)` returns the supplied default `"miss"` instead of raising, so `miss` is printed.

## Run

    python3 main.py
