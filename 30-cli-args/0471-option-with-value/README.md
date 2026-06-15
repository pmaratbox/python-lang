# 0471 — Option with value

Parse an option that takes a value using the `click` library. The `@click.option("--name")` decorator declares an option that consumes the next argv token as its string value. To stay deterministic, the command is invoked with a hardcoded argv list `["--name", "alice"]` and `standalone_mode=False` instead of the real process args, so running with no arguments always prints the same result.

## Run

    python3 main.py
