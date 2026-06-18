# 0572 — TOML table

The standard-library `tomllib` module parses TOML. Here `tomllib.loads` reads a document containing a `[server]` table with `host = "localhost"` and `port = 8080`, then we read `server.host` and `server.port` and print them as `host=<host> port=<port>`.

## Run

    python3 main.py
