# 0489 — Maximum length

Validate a string against a maximum length with the pydantic library. The model declares `code: str = Field(max_length=5)`, so the `max_length` constraint rejects any string longer than five characters. Validating `{code: 'ABCDEFG'}` raises a `ValidationError`; the program extracts the failing field name(s) from `e.errors()` (sorted and lowercased) and prints them, or `ok` when validation passes. Output is the failing field name, not any library message text.

## Run

    python3 main.py
