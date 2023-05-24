from config.db import Session
from handlers.error_handlers.error_handlers import handle_session_error
from models.Personal.PersonalModule import PersonalAPI, Personal


def create_personal(name: str, salary: int, role_id: int):
    handle_session_error(
        PersonalAPI.create,
        name=name,
        salary=salary,
        role_id=role_id,
    )


def select_all_personal():
    return handle_session_error(PersonalAPI.read_all, False)


def select_user_by_name(name: str):
    return handle_session_error(PersonalAPI.read_by_name, False, name=name)


def select_user_role(user: Personal):
    def select_role(session: Session, user):
        session.add(user)
        return user.role
    return handle_session_error(select_role, False, user=user)


def update_personal_by_id(
    id_: int,
    new_name: str | None,
    new_salary: int | None,
    new_role_id: int | None
):
    handle_session_error(
        PersonalAPI.update_by_id,
        id_=id_,
        new_name=new_name,
        new_salary=new_salary,
        new_role_id=new_role_id,
    )


def delete_personal_by_id(id_: int):
    handle_session_error(PersonalAPI.delete_by_id, id_=id_)
