# 0576 — CSV header row

Parses fixed CSV text with Python's standard-library `csv` module (`csv.reader`). The first row produced by the reader is the header, whose fields (`name`, `age`, `city`) are joined with a pipe to print `name|age|city`.

## Run

    python3 main.py
