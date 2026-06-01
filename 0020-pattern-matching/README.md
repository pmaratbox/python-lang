# 0020 — Pattern Matching

Match `n` against the literal patterns `1` and `2` with a wildcard fallback, mapping `1`, `2`, and `5` to `one`, `two`, and `many`. Python only gained structural pattern matching — the `match`/`case` statement (PEP 634) — in 3.10, so on this machine's 3.9 interpreter the equivalent is an `if`-chain that returns on the first hit. Under 3.10+ the same logic reads `match n:` with `case 1:`, `case 2:`, and a `case _:` wildcard, which can also destructure sequences, mappings, and classes.

## Run

    python3 main.py
