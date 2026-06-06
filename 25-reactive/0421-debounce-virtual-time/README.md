# 0421 — Debounce (Virtual Time)

Implement debounce(window) on a virtual-time scheduler: emit a value only after a quiet gap of `window` ticks with no newer value. Each value cancels its predecessor's pending emit via a heapq-backed scheduler whose tokens mark dead callbacks.

## Run

    python3 main.py
