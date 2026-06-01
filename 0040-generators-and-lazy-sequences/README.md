# 0040 — Generators & Lazy Sequences

Produce an endless lazy sequence of squares and take only the first three, printing `1 4 9`. A function with `yield` is a *generator*: calling it returns a lazy iterator that computes each square only when asked. `itertools.islice` pulls the first three without ever materializing the infinite stream.

## Run

    python3 main.py
