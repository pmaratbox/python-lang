# 0414 — FlatMap (mergeMap)

Implement flatMap/mergeMap: map each outer value to an inner timed stream and merge all inners concurrently (no cancellation). A heapq-backed virtual-time scheduler drives the deterministic merge.

## Run

    python3 main.py
