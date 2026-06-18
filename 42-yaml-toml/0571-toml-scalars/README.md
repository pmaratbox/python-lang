# 0571 — TOML scalars

Parse a fixed TOML document with two top-level keys using Python's standard-library `tomllib` module (added in 3.11). `tomllib.loads` returns a `dict`; the `title` key is parsed as a string and `version` as an integer. The two values are printed space-joined as `demo 2`.

## Run

    python3 main.py
