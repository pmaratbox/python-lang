# 0580 — Sum a numeric column

Uses Python's standard-library `csv` module (`csv.DictReader`) to parse the
fixed CSV text `name,age,city\nAlice,30,Paris\nBob,25,London\nCarol,35,Berlin\n`
by header name. Each row's `age` field is converted to an integer and the values
are summed (`30 + 25 + 35`) to print `90`.

## Run

    python3 main.py
