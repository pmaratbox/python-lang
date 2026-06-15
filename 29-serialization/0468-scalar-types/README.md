# 0468 — Scalar types

Serialize the scalar types `bool`, `int`, and `string` to compact JSON. Uses pydantic's `BaseModel`: fields are declared alphabetically (`active`, `count`, `label`) so the output keys come out in alphabetical order, and `model_dump_json()` emits compact JSON with no extra whitespace and lowercase booleans.

## Run

    python3 main.py
