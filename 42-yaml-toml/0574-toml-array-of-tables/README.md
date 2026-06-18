# 0574 — TOML array of tables

Parse a TOML array-of-tables (`[[servers]]`) using Python's standard-library `tomllib` module (no dependency). Each `[[servers]]` block becomes one element of the `servers` list; we collect every server's `name` and join them with commas to print `alpha,beta`.

## Run

    python3 main.py
