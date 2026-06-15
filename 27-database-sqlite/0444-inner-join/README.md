# 0444 — Inner join

Create `users` and `orders` tables in an in-memory SQLite database, populate them, then run an inner `JOIN` matching each order to its user on the `user_id`/`id` key and print each result as `name item`. Uses Python's stdlib `sqlite3` driver with `execute`/`executemany` and row iteration over the cursor.

## Run

    python3 main.py
