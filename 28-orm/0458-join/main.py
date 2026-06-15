from sqlalchemy import create_engine, String, Integer, ForeignKey, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)


class Post(Base):
    __tablename__ = "posts"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    title: Mapped[str] = mapped_column(String)


engine = create_engine("sqlite://")
Base.metadata.create_all(engine)

with Session(engine) as session:
    session.add_all([
        User(id=1, name="alice"),
        User(id=2, name="bob"),
    ])
    session.flush()
    session.add_all([
        Post(id=1, user_id=1, title="hello"),
        Post(id=2, user_id=1, title="world"),
        Post(id=3, user_id=2, title="hi"),
    ])
    session.commit()

    rows = session.execute(
        select(User.name, Post.title)
        .join(Post, Post.user_id == User.id)
        .order_by(User.name, Post.title)
    )
    for name, title in rows:
        print(name, title)
