# 0473 — Multiple values

Collect a repeated option into a list with click. The `@click.option("--num", type=int, multiple=True)` declaration makes `--num` repeatable and gathers every occurrence into a tuple. Calling `cli(["--num", "1", "--num", "2", "--num", "3"], standalone_mode=False)` parses a hardcoded argv (not the real process args, for determinism), so `num` is `(1, 2, 3)`; summing it yields `6`, which `click.echo` prints.

## Run

    python3 main.py
