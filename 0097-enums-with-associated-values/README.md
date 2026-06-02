# 0097 — Enums with Associated Values

Define a shape type carrying associated data — `Rect(2, 3)` and `Square(4)` — compute each area by matching on the variant, and print `6` and `16`. Python has no native sum type; separate classes carry the associated data and `isinstance` dispatches (3.10+ `match` can also destructure them).

## Run

    python3 main.py
