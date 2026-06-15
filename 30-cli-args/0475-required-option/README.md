# 0475 — Required option

Declare a CLI option as required. Uses `click`'s `@click.option` with `required=True`: the parser rejects argv that omits `--id` and accepts the integer value when present. To stay deterministic, it parses a fixed argv `["--id", "42"]` passed straight to the command instead of the real process args, printing `42` via `click.echo`.

## Run

    python3 main.py
