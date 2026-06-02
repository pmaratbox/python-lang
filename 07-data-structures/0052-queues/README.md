# 0052 — Queues

Enqueue `1`, `2`, and `3` into a queue, then dequeue them all and print them in first-in-first-out order: `1 2 3`. `collections.deque` is the double-ended queue: `append` adds at the back and `popleft()` removes from the front in O(1). A plain list works too, but `pop(0)` is O(n).

## Run

    python3 main.py
