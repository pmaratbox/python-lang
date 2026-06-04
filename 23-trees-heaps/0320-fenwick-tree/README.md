# 0320 — Fenwick Tree Prefix Sum

Build a Fenwick (BIT) tree over [1,2,3,4,5] and query the prefix sum of the first 4 elements, printing `10`. The low-bit trick `i & (-i)` walks index ranges during update and query.

## Run

    python3 main.py
