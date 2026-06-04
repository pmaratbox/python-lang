# 0326 — Monoid Fold

Fold lists under two monoids: string concat ["a","b","c"]->"abc" and integer sum [1,2,3]->6, printing `abc 6`. A generic `fold` over `functools.reduce` takes the identity and combine op for each monoid.

## Run

    python3 main.py
