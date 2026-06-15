from sqlalchemy import create_engine, String, Integer, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    age: Mapped[int] = mapped_column(Integer)


engine = create_engine("sqlite://")
Base.metadata.create_all(engine)

with Session(engine) as session:
    session.add_all([
        User(id=1, name="alice", age=30),
        User(id=2, name="bob", age=25),
        User(id=3, name="carol", age=35),
    ])
    session.commit()

    for user in session.scalars(select(User).order_by(User.id)):
        print(user.name)
