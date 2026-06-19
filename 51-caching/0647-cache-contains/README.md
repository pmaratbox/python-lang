# 0647 — Contains key

Uses the real `cachetools.LRUCache` (a strict LRU cache) with `maxsize=3`. After
putting `a=1`, we use the `in` operator to test key membership: `a` is present
and `x` is not. In cachetools a membership check does not promote recency, so it
is a pure lookup. The two booleans are printed lowercase, space-joined.

## Run

    python3 main.py
