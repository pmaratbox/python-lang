# 0465 — Round trip

Serialize a typed object and then parse it straight back. Uses pydantic's `BaseModel`: `model_dump_json()` serializes the `Person` to a compact JSON string (keys alphabetical because fields are declared in alphabetical order), and `model_validate_json()` parses that string back into a `Person`, whose `name` is then printed.

## Run

    python3 main.py
