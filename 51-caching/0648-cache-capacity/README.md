# 0648 — Capacity bound

Uses the real `cachetools.LRUCache` (a strict LRU cache). With `maxsize=3` we
insert four keys `a, b, c, d`. The cache enforces its capacity by evicting the
least-recently-used entry on each overflow, so `len(cache)` is capped at 3
rather than 4.

## Run

    python3 main.py
