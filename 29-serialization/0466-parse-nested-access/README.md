# 0466 — Parse & access nested

Parse a JSON string and read a deeply nested value. Uses Python's standard-library `json` module: `json.loads` parses the text into a dynamic `dict`/`list` tree, then ordinary key and index access (`data["user"]["name"]` and `data["user"]["roles"][0]`) reaches the nested name and the first role.

## Run

    python3 main.py
