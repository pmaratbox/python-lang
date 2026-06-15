# 0490 — Email format

Validate an object with the pydantic library. The `email` field is constrained by `Field(pattern=...)`, a regex that requires a single `@` and a dotted domain, so `email="not-an-email"` fails. The output is the failing field name(s) — extracted from pydantic's `ValidationError.errors()` via each error's `loc`, lowercased and sorted — or `ok` if validation passes.

## Run

    python3 main.py
