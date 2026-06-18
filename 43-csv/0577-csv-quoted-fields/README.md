# 0577 — Quoted CSV fields

Uses Python's stdlib `csv` library to parse `name,note\nAlice,"hello, world"\n`. The
`csv.reader` correctly handles the quoted field, keeping the embedded comma as part of
the value instead of splitting on it. We print the `note` value of the data row.

## Run

    python3 main.py
