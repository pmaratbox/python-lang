# 0635 — List value

Uses the real `pydantic-settings` configuration library to load `config.json` via a `JsonConfigSettingsSource` into a typed `Settings(BaseSettings)` model. The `hosts` field is parsed as a `list[str]`, then joined with commas to print `a,b,c`.

## Run

    python3 main.py
