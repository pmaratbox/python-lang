# 0074 — Run-Length Encoding

Run-length encode the string `aaabbc` (each run of a repeated character becomes the character followed by its count), printing `a3b2c1`. The inner loop counts how far the current character repeats, then appends `char + count`; the outer loop moves to the next run.

## Run

    python3 main.py
