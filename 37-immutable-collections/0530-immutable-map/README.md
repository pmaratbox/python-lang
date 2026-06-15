# 0530 — Immutable map

Use the `pyrsistent` persistent collection library: build an immutable `pmap` `{a: 1}`, then call `.set("b", 2)`, which RETURNS A NEW map instead of mutating in place. The new map has keys `a b` while the original is UNCHANGED with just `a`. Keys are sorted before printing for deterministic output.

## Run

    python3 main.py
