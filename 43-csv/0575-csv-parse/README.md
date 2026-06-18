# 0575 — Parse CSV rows

Uses Python's standard-library `csv` module (`csv.reader`) to parse the fixed
CSV text `name,age,city\nAlice,30,Paris\nBob,25,London\nCarol,35,Berlin\n` into
rows. The header row is skipped and the first column (the name) of each data row
is joined with commas.

## Run

    python3 main.py
