# 0536 — Nested update

Use the `pyrsistent` persistent collection library: build a nested immutable `pmap` `{user: {age: 30}}`, then call `.transform(["user", "age"], 31)`, which walks the path and RETURNS A NEW map instead of mutating in place. The new map has the nested age `31` while the original is UNCHANGED at `30`.

## Run

    python3 main.py
