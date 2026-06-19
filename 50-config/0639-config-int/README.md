# 0639 — Integer value

Uses **pydantic-settings** to load `config.json` into a typed `Settings` model and reads the integer field `retries`. Pydantic coerces the JSON value to an `int`, and we print it.

## Run

    python3 main.py
