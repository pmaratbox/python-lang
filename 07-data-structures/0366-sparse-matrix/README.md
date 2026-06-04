# 0366 — Sparse Matrix

Store only nonzero entries; with (1,1)=5 set, read (1,1) (5) and (0,0) (0), printing `5 0`. A dict keyed by the (row, col) tuple holds only nonzero cells, and dict.get supplies 0 for missing keys.

## Run

    python3 main.py
