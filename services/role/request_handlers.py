from handlers.error_handlers.error_handlers import handle_session_error
from models.Role.RoleModule import RoleAPI


def create_role(role_name: str):
    handle_session_error(
        RoleAPI.create,
        role_name=role_name,
    )


def select_all_role():
    return handle_session_error(RoleAPI.read_all, False)


def update_role_by_id(id_: int, new_role_name: str | None):
    handle_session_error(
        RoleAPI.update_by_id,
        id_=id_,
        new_role_name=new_role_name,
    )


def delete_role_by_id(id_: int):
    handle_session_error(RoleAPI.delete_by_id, id_=id_)
