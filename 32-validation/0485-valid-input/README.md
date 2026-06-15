# 0485 — Valid input

Uses the [pydantic](https://docs.pydantic.dev/) library to validate an object against a schema where `name` must have `min_length=3` and `age` must satisfy `ge=0, le=120`. The input `{name: alice, age: 30}` meets every constraint, so validation passes. The output is the sorted, lowercased failing field name(s) extracted from the `ValidationError` (one per line), or `ok` when validation passes — as here.

## Run

    python3 main.py
