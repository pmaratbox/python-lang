# 0441 — Aggregate functions

Compute count, sum, min, and max over a table of integer amounts using a single SQL query. Creates an in-memory table `t`, inserts 10, 20, 30, 40, 50, then runs `select count(*),sum(amount),min(amount),max(amount) from t` and prints the four values, each on its own line. Uses Python's stdlib `sqlite3` driver.

## Run

    python3 main.py
