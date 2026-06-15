# 0455 — Count

Defines a `User` model over an in-memory SQLite database with SQLAlchemy 2.0's declarative ORM (`DeclarativeBase`, `Mapped`, `mapped_column`), inserts three rows via a `Session`, then counts all users with the `func.count()` aggregate through `select(func.count()).select_from(User)`. The single scalar result is fetched with `session.scalar(...)` and printed.

## Run

    python3 main.py
