# 0451 — Order by

Defines a `User` model over an in-memory SQLite database with SQLAlchemy 2.0's declarative ORM (`DeclarativeBase`, `Mapped`, `mapped_column`), inserts three rows via a `Session`, then queries every user sorted by age ascending using `select(User).order_by(User.age)`. Each name is printed on its own line in age order.

## Run

    python3 main.py
