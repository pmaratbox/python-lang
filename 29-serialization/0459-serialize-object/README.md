# 0459 — Serialize an object

Serialize a typed object to a compact JSON string. Uses `pydantic`'s `BaseModel`: declaring the fields `age` and `name` in alphabetical order makes `model_dump_json()` emit compact JSON (no spaces) with keys already in alphabetical order — `{"age":30,"name":"alice"}`.

## Run

    python3 main.py
