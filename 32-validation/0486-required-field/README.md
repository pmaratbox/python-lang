# 0486 — Required field

Validate input with the pydantic library. The `Person` model declares `name` and `age` as required fields on a `BaseModel`; a field with no default is mandatory, so when the input supplies `name` but omits `age`, pydantic raises a `ValidationError` whose error object reports `age` as missing. The output is the sorted, lowercased failing field name(s) pulled from `err.errors()` (here, `age`), or `ok` when validation passes.

## Run

    python3 main.py
