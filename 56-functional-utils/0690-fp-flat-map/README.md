# 0690 — Flat map

Python's `toolz` library applies a flat-map over `[1,2,3]` with `toolz.mapcat`, which maps each element to a list (`x -> [x, x*10]`) and concatenates the results into one flat stream, then comma-joins them to produce `1,10,2,20,3,30`.

## Run

    python3 main.py
