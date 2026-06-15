# 0472 — Default value

Use click's option default when the flag is absent. The `@click.option("--count", type=int, default=1)` declaration gives `--count` a fallback value, and calling `cli([], standalone_mode=False)` parses a hardcoded empty argv (not the real process args, for determinism), so `count` falls back to the default `1` which `click.echo` prints.

## Run

    python3 main.py
