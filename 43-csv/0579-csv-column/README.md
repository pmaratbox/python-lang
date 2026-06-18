# 0579 — Extract a column

Uses Python's stdlib `csv` library to parse the `name,age,city` CSV with
`csv.DictReader`, which maps each data row to a dict keyed by header name. We
extract the `age` column by name from every row and join the values with commas,
producing `30,25,35`.

## Run

    python3 main.py
