# 0492 — Custom rule

Validate with the pydantic library. A `@field_validator` on `password` implements a custom rule: the value must contain at least one digit. The input `{password: 'abcdef'}` has no digit, so validation raises `ValidationError`. The output is the failing field name(s) — extracted from the error object's `loc`, lowercased and sorted — here `password`.

## Run

    python3 main.py
