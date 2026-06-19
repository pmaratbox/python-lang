# 0640 — Read a section

Uses the real `pydantic-settings` configuration library to load `config.json` via `JsonConfigSettingsSource` into a typed `Settings` model. The nested `server` section is modeled as a `Server` submodel, and both `server.host` and `server.port` are read and printed as `host:port`.

## Run

    python3 main.py
