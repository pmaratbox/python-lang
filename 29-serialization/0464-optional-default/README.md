# 0464 — Optional field default

Parse JSON that is missing a field, falling back to a declared default. Uses pydantic's `BaseModel`: `Person` declares `age: int = 0` (alphabetical fields), so `model_validate_json` accepts the JSON `{"name":"alice"}` where `age` is absent and fills it with the default `0`. Printing `name age` yields `alice 0`.

## Run

    python3 main.py
