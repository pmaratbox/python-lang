# 0634 — Nested key

Uses **pydantic-settings** to load `config.json` into a typed `Settings` model and read the nested key `server.port` (an integer), which resolves to `8080`.

## Run

    python3 main.py
