# 0050 — Stacks

Push `1`, `2`, and `3` onto a stack, then pop them all off and print them in last-in-first-out order: `3 2 1`. A plain `list` is a stack: `append` pushes onto the end and `pop()` (with no index) removes and returns the last item, giving LIFO order. For a pure stack a list is ideal; `collections.deque` only helps when you also push and pop at the front.

## Run

    python3 main.py
