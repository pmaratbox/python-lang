# 0047 — Immutable Update (Copy-with)

Make a copy of the point `(1, 2)` with its `x` changed to `9`, leaving the original intact, and print `original: (1, 2)` then `updated: (9, 2)`. `dataclasses.replace` builds a new instance, copying every field and overriding the ones you name — here `x=9`. The frozen original is untouched, so immutable values are updated by replacement.

## Run

    python3 main.py
