# 0462 — Array of objects

Serialize a Python list of objects to a JSON array. Uses pydantic's `TypeAdapter(list[Person])` together with `dump_json`, which renders the whole list as one compact JSON array. Each `Person` has its fields declared alphabetically (`age`, `name`), so the serialized keys come out in alphabetical order with no extra whitespace.

## Run

    python3 main.py
