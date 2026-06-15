# 0476 — Choice option

Restrict an option to a fixed set of choices using click's `click.Choice`. The `@click.option("--color", type=click.Choice(["red", "green", "blue"]))` declaration validates that the value is one of `red`, `green`, or `blue`, and calling `cli(["--color", "green"], standalone_mode=False)` parses a hardcoded argv (not the real process args, for determinism), so `click.echo` prints the chosen value `green`.

## Run

    python3 main.py
