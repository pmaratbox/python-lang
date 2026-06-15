# 0529 — Immutable list

Use the `pyrsistent` persistent collection library: build a `pvector([1, 2, 3])` and call `.append(4)`, which RETURNS A NEW vector rather than mutating in place. Printing the new vector then the original shows the original is unchanged.

## Run

    python3 main.py
