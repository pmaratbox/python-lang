# 0488 — Number range

Validate an object with the pydantic library. The `age` field is constrained to the range 0..120 using `Field(ge=0, le=120)`. Validating `{name: 'alice', age: 200}` raises a `ValidationError` because 200 exceeds the upper bound. The output is the failing field name(s) — extracted from each error's `loc` in `err.errors()`, lowercased, deduped and sorted — here `age`.

## Run

    python3 main.py
