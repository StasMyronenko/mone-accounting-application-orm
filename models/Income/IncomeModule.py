from sqlalchemy import Integer, String, ForeignKey, select, Sequence, Row, RowMapping
from sqlalchemy.dialects.postgresql import Any
from sqlalchemy.orm import mapped_column, Mapped, relationship, Session

from models.Base import Base
from models.Product.ProductModule import Product

import models.Income.data as data
import models.BankAccount.data as bank_account_data
import models.IncomeProduct.data as income_product_data


class IncomeAPI:
    @staticmethod
    def create(
            session: Session,
            sum_: int,
            from_account: str,
            bank_account_id: int,
            products: list["Product"]
    ):
        income = Income(
            sum=sum_,
            from_account=from_account,
            bank_account_id=bank_account_id,
            poducts=products
        )
        session.add(income)
        session.commit()

    @staticmethod
    def read_all(session: Session) -> Sequence[Row | RowMapping | Any | "Income"]:
        statement = select(Income)
        return session.scalars(statement).all()

    @staticmethod
    def update_by_id(
            session: Session,
            id_: int,
            new_sum: int | None,
            new_from_account: str | None,
            new_bank_account_id: int | None,
            new_products: list["Product"] | None
    ):
        income = session.get(Income, id_)

        if new_sum:
            income.sum = new_sum

        if new_from_account:
            income.from_account = new_from_account

        if new_bank_account_id:
            income.bank_account_id = new_bank_account_id

        if new_products:
            income.products = new_products

        session.commit()

    @staticmethod
    def delete_by_id(session: Session, id_: int):
        income = session.get(Income, id_)
        session.delete(income)
        session.commit()


class Income(Base):
    __tablename__ = data.tablename

    id: Mapped[int] = mapped_column(data.id_, Integer, primary_key=True)
    sum: Mapped[str] = mapped_column(data.sum_, Integer, default=0, nullable=False)
    from_account: Mapped[str] = mapped_column(data.from_account, String)
    bank_account_id: Mapped[int] = mapped_column(
        data.bank_account_id,
        ForeignKey(f'{bank_account_data.tablename}.{bank_account_data.id_}')
    )
    products: Mapped[list["Product"]] = relationship(
        secondary=income_product_data.tablename
    )
