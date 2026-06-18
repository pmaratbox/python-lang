# 0581 — Custom delimiter

Uses Python's stdlib `csv` library to parse semicolon-delimited text `a;b;c\n1;2;3\n` by passing `delimiter=";"` to `csv.reader`. It then takes the second (data) row's fields and joins them with commas to print `1,2,3`.

## Run

    python3 main.py
