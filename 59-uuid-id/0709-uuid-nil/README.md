# 0709 — Nil UUID

Python's stdlib `uuid` module constructs the nil (all-zero) UUID with `uuid.UUID(int=0)`. Printing it yields the canonical lowercase form, which for the nil UUID is all zeros.

## Run

    python3 main.py
