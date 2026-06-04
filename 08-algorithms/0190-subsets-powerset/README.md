# 0190 — Subsets (Power Set)

Generate the power set of [1,2,3] in bitmask order 0..7 (empty printed as `{}`), one subset per line space-separated. A list comprehension tests each bit with `mask & (1 << i)`.

## Run

    python3 main.py
