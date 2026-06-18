# 0582 — Filter rows

Uses Python's standard-library `csv` module (`csv.DictReader`) to parse the
fixed CSV text `name,age,city\nAlice,30,Paris\nBob,25,London\nCarol,35,Berlin\n`
by header name. Data rows are filtered with the predicate `age > 28` (keeping
Alice 30 and Carol 35, excluding Bob 25), and the kept names are joined with
commas.

## Run

    python3 main.py
