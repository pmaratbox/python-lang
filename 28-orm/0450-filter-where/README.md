# 0450 — Filter with where

Query rows matching a condition with SQLAlchemy 2.0's ORM. A `User` model is mapped with `DeclarativeBase`/`Mapped`/`mapped_column`, rows are inserted through a `Session`, and `select(User).where(User.age >= 30).order_by(User.id)` builds the filtered query whose `name` column is printed for each matching row.

## Run

    python3 main.py
