# 0467 — Field rename

Map a code field name to a different JSON key. Uses `pydantic`'s `Field(serialization_alias=...)`: the model's Python attribute `fullName` is emitted under the JSON key `full_name` when `model_dump_json(by_alias=True)` serializes the object, producing compact JSON — `{"full_name":"alice"}`.

## Run

    python3 main.py
