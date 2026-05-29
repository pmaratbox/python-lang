# 0013 — Optional

Hold one value that is present (`42`) and one that is absent, then print each
with a fallback of `-1` when absent. Python has no Option type — `None`
represents absence, and the type hint is `Optional[int]` (equivalently
`int | None` on Python 3.10+). Default with an explicit `x if x is not None else
-1`, since `x or -1` would also replace a legitimate `0`.

## Run

    python3 main.py
