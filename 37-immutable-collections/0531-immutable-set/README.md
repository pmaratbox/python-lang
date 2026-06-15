# 0531 — Immutable set

Use the `pyrsistent` library's persistent `pset`: calling `.add(4)` on the set `{1, 2, 3}` RETURNS A NEW set rather than mutating in place, so the original `pset` is left unchanged. The program prints the size of the new set, then the size of the original to prove it was not modified.

## Run

    python3 main.py
