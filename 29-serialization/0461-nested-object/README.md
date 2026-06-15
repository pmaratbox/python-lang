# 0461 — Nested object

Serialize an object that contains another object. Uses pydantic's `BaseModel`: a `Person` model holds an `Address` model as a field, and `model_dump_json()` recursively serializes the nested model into compact JSON. Declaring fields alphabetically (`address` before `name`, `city` before `zip`) yields alphabetically ordered keys.

## Run

    python3 main.py
