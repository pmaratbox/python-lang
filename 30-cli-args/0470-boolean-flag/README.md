# 0470 — Boolean flag

Parse a boolean flag with `click`. The `--verbose` option declared with `is_flag=True` becomes a Python `bool` that is `True` when the flag is present. The parser runs over a fixed, hardcoded argv `["--verbose"]` (passed to `cli(..., standalone_mode=False)`) rather than the real process arguments, so the output is deterministic — printing the value lowercased gives `true`.

## Run

    python3 main.py
