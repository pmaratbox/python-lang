# 0487 — Minimum length

Validate data with the pydantic library. The `name` field is declared as `str = Field(min_length=3)`, so the input `{name: "al", age: 30}` violates pydantic's `min_length` constraint and raises a `ValidationError`. The program prints the lowercased, sorted failing field name(s) extracted from `e.errors()` (here `name`), or `ok` when validation passes.

## Run

    python3 main.py
