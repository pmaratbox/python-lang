# 0644 — Recency promotion

Uses `cachetools.LRUCache`, Python's strict LRU cache library, with capacity 3. After putting `a`, `b`, `c`, a read of `a` (`cache["a"]`) promotes it to most-recently-used. Inserting `d` then overflows the cache and evicts the now-least-recently-used key `b`. Looking up `a` returns its value while `b` reports `miss`.

## Run

    python3 main.py
