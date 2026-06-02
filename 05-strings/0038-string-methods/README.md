# 0038 — String Methods

Split `"a,b,c"` on commas, upper-case each part, and join them with `-`, printing `A-B-C`. `str.split(",")` returns a list of parts, a comprehension upper-cases each with `str.upper()`, and `"-".join(...)` stitches them back. Strings are immutable, so every method returns a new string.

## Run

    python3 main.py
