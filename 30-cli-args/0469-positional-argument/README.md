# 0469 — Positional argument

Parse a positional argument with click. The `@click.argument("name")` decorator declares a single required positional parameter, and `click.echo` prints it. To stay deterministic, the command is invoked with a fixed argv list `["alice"]` and `standalone_mode=False` instead of reading the real process arguments, so running with no arguments always prints the same output.

## Run

    python3 main.py
