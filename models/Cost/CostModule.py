from sqlalchemy import Integer, String, ForeignKey, select, Sequence, Row, RowMapping
from sqlalchemy.dialects.postgresql import Any
from sqlalchemy.orm import Mapped, mapped_column, Session

from models.Base import Base
import models.Cost.data as data
import models.BankAccount.data as bank_account_data
import models.Personal.data as personal_data


class CostAPI:
    @staticmethod
    def create(
            session: Session, sum_: int,
            bank_account_id: int,
            to_account: str,
            description: str,
            responsible_person_id: int
    ):
        cost = Cost(
            sum=sum_,
            bank_account_id=bank_account_id,
            to_account=to_account,
            pay_item_description=description,
            responsible_person_id=responsible_person_id
        )
        session.add(cost)
        session.commit()

    @staticmethod
    def read_all(session: Session) -> Sequence[Row | RowMapping | Any | "Cost"]:
        statement = select(Cost)
        costs = session.scalars(statement).all()
        return costs

    @staticmethod
    def update_by_id(
            session: Session,
            id_: int,
            new_sum: int | None,
            new_bank_account_id: int | None,
            new_to_account: str | None,
            new_description: str | None,
            new_responsible_person_id: int | None
    ):
        cost = session.get(Cost, id_)
        if new_sum:
            cost.sum = new_sum

        if new_bank_account_id:
            cost.bank_account_id = new_bank_account_id

        if new_to_account:
            cost.to_account = new_to_account

        if new_description:
            cost.pay_item_description = new_description

        if new_responsible_person_id:
            cost.responsible_person_id = new_responsible_person_id

        session.commit()

    @staticmethod
    def delete_by_id(session: Session, id_: int):
        cost = session.get(Cost, id_)
        session.delete(cost)
        session.commit()


class Cost(Base):
    __tablename__ = data.tablename

    id: Mapped[int] = mapped_column(data.id_, Integer, primary_key=True)
    sum: Mapped[int] = mapped_column(data.sum_, Integer, default=0, nullable=False)
    bank_account_id: Mapped[int] = mapped_column(data.bank_account_id, ForeignKey(
        f'{bank_account_data.tablename}.{bank_account_data.id_}'
    ))
    to_account: Mapped[str] = mapped_column(data.to_account, String, nullable=False)
    pay_item_description: Mapped[str] = mapped_column(data.pay_item_description, String)
    responsible_person_id: Mapped[int] = mapped_column(data.responsible_person_id, ForeignKey(
        f'{personal_data.tablename}.{personal_data.id_}'
    ))
