# 0645 — Cache size

Uses the real `cachetools.LRUCache` (a strict LRU cache). With `maxsize=5` we
put two keys `a` and `b`. Since the capacity (5) is larger than the number of
entries, nothing is evicted and `len(cache)` reports the live entry count `2`.

## Run

    python3 main.py
