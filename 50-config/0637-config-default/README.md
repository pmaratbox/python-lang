# 0637 — Default for missing key

Uses `pydantic-settings`, Python's configuration library, to load `config.json` into a typed `Settings` model. The key `missing` is absent from the file, so the library falls back to the field's declared default `"fallback"`, which is then printed.

## Run

    python3 main.py
