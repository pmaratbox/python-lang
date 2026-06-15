from sqlalchemy import create_engine, String, Integer, select, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session


class Base(DeclarativeBase):
    pass


class Product(Base):
    __tablename__ = "products"
    id: Mapped[int] = mapped_column(primary_key=True)
    category: Mapped[str] = mapped_column(String)
    price: Mapped[int] = mapped_column(Integer)


engine = create_engine("sqlite://")
Base.metadata.create_all(engine)

with Session(engine) as session:
    session.add_all([
        Product(id=1, category="a", price=10),
        Product(id=2, category="b", price=20),
        Product(id=3, category="a", price=30),
    ])
    session.commit()

    rows = session.execute(
        select(Product.category, func.sum(Product.price))
        .group_by(Product.category)
        .order_by(Product.category)
    )
    for category, total in rows:
        print(category, total)
