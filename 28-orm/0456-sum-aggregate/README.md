# 0456 — Sum aggregate

Compute a column total with SQLAlchemy 2.0's ORM. Defines a `User` model via `DeclarativeBase`/`Mapped`/`mapped_column`, inserts three rows into an in-memory SQLite database, then runs `select(func.sum(User.age))` through a `Session` and prints the total (90). The aggregate is expressed with the query-builder API rather than a raw SQL string.

## Run

    python3 main.py
