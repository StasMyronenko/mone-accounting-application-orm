from sqlalchemy import Integer, String, Sequence, Row, RowMapping, select
from sqlalchemy.dialects.postgresql import Any
from sqlalchemy.orm import mapped_column, Mapped, Session

from models.Base import Base
import models.Role.data as data


class RoleAPI:
    @staticmethod
    def create(session: Session, role_name: str):
        role = Role(role_name=role_name)
        session.add(role)
        session.commit()

    @staticmethod
    def read_all(session: Session) -> Sequence[Row | RowMapping | Any | "Role"]:
        statement = select(Role)
        return session.scalars(statement).all()

    @staticmethod
    def update_by_id(session: Session, id_: int, new_role_name: str | None):
        role = session.get(Role, id_)
        if new_role_name:
            role.role_name = new_role_name
        session.commit()

    @staticmethod
    def delete_by_id(session: Session, id_: int) -> None:
        role = session.get(Role, id_)
        session.delete(role)
        session.commit()


class Role(Base):
    __tablename__ = data.tablename

    id: Mapped[int] = mapped_column(data.id_, Integer, primary_key=True)
    role_name: Mapped[str] = mapped_column(data.role_name, String, nullable=False)
