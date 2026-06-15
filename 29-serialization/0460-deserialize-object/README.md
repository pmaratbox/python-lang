# 0460 — Deserialize an object

Parse a JSON string into a typed object using pydantic's `BaseModel.model_validate_json`. The `Person` model declares its fields in alphabetical order (`age`, `name`); `model_validate_json` reads the JSON `{"age":30,"name":"alice"}`, validates and coerces the values into typed attributes, and the parsed `name` and `age` are printed.

## Run

    python3 main.py
