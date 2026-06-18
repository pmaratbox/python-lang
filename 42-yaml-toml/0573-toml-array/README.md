# 0573 — TOML array

Parses the fixed TOML document `tags = ["red", "green", "blue"]` with Python's standard-library `tomllib` module (`tomllib.loads`). TOML arrays decode to Python lists, so the parsed `tags` list is joined with commas to print `red,green,blue`.

## Run

    python3 main.py
