from __future__ import annotations

from sqlalchemy import Integer, String, ForeignKey, Sequence, Row, RowMapping, select
from sqlalchemy.dialects.postgresql import Any
from sqlalchemy.orm import mapped_column, Mapped, Session

from models.Base import Base
from models.Role.RoleModule import Role
import models.Personal.data as data


class PersonalAPI:
    @staticmethod
    def create(session: Session, name: str, salary: int, role_id: int):
        person = Personal(name=name, salary=salary, role_id=role_id)
        session.add(person)

    @staticmethod
    def read_all(session: Session) -> Sequence[Row | RowMapping | Any | "Personal"]:
        statement = select(Personal)
        return session.scalars(statement).all()

    @staticmethod
    def update_by_id(
        session: Session,
        id_: int,
        new_name: str | None,
        new_salary: int | None,
        new_role_id: int | None
    ):
        person = session.get(Personal, id_)
        if new_name:
            person.name = new_name

        if new_salary:
            person.salary = new_salary

        if new_role_id:
            person.role_id = new_role_id

    @staticmethod
    def delete_by_id(session: Session, id_: int):
        person = session.get(Personal, id_)
        session.delete(person)


class Personal(Base):
    __tablename__ = data.tablename

    id: Mapped[int] = mapped_column(data.id_, Integer, primary_key=True)
    name: Mapped[str] = mapped_column(data.name, String)
    salary: Mapped[int] = mapped_column(data.salary, Integer)
    role_id: Mapped[int] = mapped_column(
        data.role_id,
        ForeignKey(f'{Role.__tablename__}.{Role.id.key}', ondelete='SET NULL'),
        nullable=True
    )
