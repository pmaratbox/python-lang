# 0638 — Env override

Uses **pydantic-settings** to load `config.json` and then resolve `name`. By ordering the sources so `env_settings` comes before the `JsonConfigSettingsSource`, an in-process environment variable (`NAME=from-env`, set before constructing `Settings`) takes higher priority than the file's `name=myapp`, so the resolved value is `from-env`.

## Run

    python3 main.py
