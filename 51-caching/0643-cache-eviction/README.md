# 0643 — LRU eviction

Uses the real `cachetools.LRUCache` (a strict LRU cache) with `maxsize=3`. We
insert `a, b, c, d` with no reads in between, so recency follows insertion
order. The fourth put overflows capacity and the cache evicts the
least-recently-used key, `a`. Looking up `a` then yields the `miss` default
while `d` returns `4`.

## Run

    python3 main.py
