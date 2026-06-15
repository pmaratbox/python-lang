# 0452 — Limit

Defines a `User` model with SQLAlchemy 2.0's declarative ORM (`DeclarativeBase`, `Mapped`, `mapped_column`), seeds three rows into an in-memory SQLite database, then builds a query with `select(User).order_by(User.age.desc()).limit(2)` and iterates it via `Session.scalars` to take only the top two rows by age. Printing each name yields `carol` (35) then `alice` (30).

## Run

    python3 main.py
