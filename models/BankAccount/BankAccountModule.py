from typing import Any, Sequence

from sqlalchemy import Integer, String, Row, RowMapping
from sqlalchemy import select
from sqlalchemy.orm import mapped_column, Mapped, Session

from models.Base import Base
import models.BankAccount.data as data


class BankAccountAPI:
    @staticmethod
    def create(session: Session, number: str, name: str) -> None:
        bank_account = BankAccount(number=number, name=name)
        session.add(bank_account)
        session.commit()

    @staticmethod
    def read_all(session: Session) -> Sequence[Row | RowMapping | Any | "BankAccount"]:
        statement = select(BankAccount)
        bank_accounts = session.scalars(statement).all()
        return bank_accounts

    @staticmethod
    def update_by_id(session: Session, id_: int, new_number: str | None, new_name: str | None):
        bank_account = session.get(BankAccount, id_)
        if new_number:
            bank_account.number = new_number
        if new_name:
            bank_account.name = new_name
        session.commit()

    @staticmethod
    def delete_by_id(session: Session, id_: int) -> None:
        bank_account = session.get(BankAccount, id_)
        session.delete(bank_account)
        session.commit()


class BankAccount(Base):
    __tablename__ = data.tablename

    id: Mapped[int] = mapped_column(data.id_, Integer, primary_key=True, unique=True)
    number: Mapped[str] = mapped_column(data.number, String(16), unique=True)
    name: Mapped[str] = mapped_column(data.name, String)
