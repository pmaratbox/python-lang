# 0463 — Array of primitives

Serialize a list of integers to a compact JSON array using pydantic's `TypeAdapter`. A `TypeAdapter(list[int])` validates and serializes plain Python types that aren't `BaseModel` subclasses; its `dump_json` method produces compact JSON bytes (no spaces) which we decode to a string and print.

## Run

    python3 main.py
