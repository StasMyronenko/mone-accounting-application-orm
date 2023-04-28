from __future__ import annotations

from sqlalchemy import Integer, String, Sequence, Row, RowMapping, select
from sqlalchemy.dialects.postgresql import Any
from sqlalchemy.orm import Mapped, mapped_column, Session

from models.Base import Base

import models.Product.data as data


class ProductAPI:
    @staticmethod
    def create(session: Session, name: str, description: str, price: int):
        product = Product(name=name, description=description, price=price)
        session.add(product)
        session.commit()

    @staticmethod
    def read_all(session: Session) -> Sequence[Row | RowMapping | Any | "Product"]:
        statement = select(Product)
        return session.scalars(statement).all()

    @staticmethod
    def update_by_id(
            session: Session,
            id_: int,
            new_name: str | None,
            new_description: str | None,
            new_price: int | None
    ):
        product = session.get(Product, id_)
        if new_name:
            product.name = new_name

        if new_description:
            product.description = new_description

        if new_price:
            product.price = new_price

        session.commit()

    @staticmethod
    def delete_by_id(session: Session, id_: int) -> None:
        product = session.get(Product, id_)
        session.delete(product)
        session.commit()


class Product(Base):
    __tablename__ = data.tablename

    id: Mapped[int] = mapped_column(data.id_, Integer, primary_key=True)
    name: Mapped[str] = mapped_column(data.name, String)
    description: Mapped[str] = mapped_column(data.description, String)
    price: Mapped[int] = mapped_column(data.price, Integer, nullable=False)
