# 0412 — Combine Latest

Implement combineLatest of two timed streams, emitting the pair of latest values whenever either source emits (once both have emitted). Closures with `nonlocal` hold each source's latest value, and a heapq-backed virtual clock drives deterministic emission.

## Run

    python3 main.py
