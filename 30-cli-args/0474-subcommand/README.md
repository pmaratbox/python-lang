# 0474 — Subcommand

Dispatch to a subcommand. Uses `click`'s `@click.group` to define a parent command and `@cli.command` to register an `add` subcommand taking two integer positionals (`@click.argument(..., type=int)`). Calling `cli(["add", "2", "3"], standalone_mode=False)` parses a fixed argv for determinism, dispatches to `add`, sums the arguments and prints `5`.

## Run

    python3 main.py
