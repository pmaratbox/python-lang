# 0491 — Multiple errors

Using the real [pydantic](https://docs.pydantic.dev/) library, a `BaseModel` declares
`name` with `Field(min_length=3)` and `age` with `Field(ge=0, le=120)`. pydantic does not
fail fast: validating `{name: "al", age: 200}` raises a single `ValidationError` that
collects every constraint violation. We read `err.errors()`, take each failing field name
from `loc[0]`, lowercase, dedupe, and sort them. The output is the failing field name(s),
one per line (or `ok` when validation passes) — never the library's message text.

## Run

    python3 main.py
