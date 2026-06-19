# 0646 — Update a value

Uses the real `cachetools.LRUCache` (a strict LRU cache). We put `a=1` and then
put `a=2` using the same key. Because the key already exists, the LRU cache
updates the stored value in place instead of creating a second entry, so reading
`a` back yields the latest value `2`.

## Run

    python3 main.py
