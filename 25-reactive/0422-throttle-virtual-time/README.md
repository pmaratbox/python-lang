# 0422 — Throttle (Virtual Time)

Implement throttle(window) (leading edge) on a virtual-time scheduler: emit a value, then suppress further values for `window` ticks. A `nonlocal` closure variable tracks `block_until` while `heapq` orders the scheduled events.

## Run

    python3 main.py
