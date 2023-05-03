from handlers.error_handlers.error_handlers import handle_session_error
from models.Cost.CostModule import CostAPI


def create_cost(
    sum_: int,
    bank_account_id: int,
    to_account: str,
    description: str,
    responsible_person_id: int
):
    if len(to_account) != 16:
        raise Exception('account number length should be 16 characters')
    handle_session_error(
        CostAPI.create,
        sum_=sum_,
        bank_account_id=bank_account_id,
        to_account=to_account,
        description=description,
        responsible_person_id=responsible_person_id
    )


def select_all_cost():
    return handle_session_error(CostAPI.read_all, False)


def update_cost_by_id(
    id_: int,
    new_sum: int | None,
    new_bank_account_id: int | None,
    new_to_account: str | None,
    new_description: str | None,
    new_responsible_person_id: int | None
):
    handle_session_error(
        CostAPI.update_by_id,
        id_=id_,
        new_sum=new_sum,
        new_bank_account_id=new_bank_account_id,
        new_to_account=new_to_account,
        new_description=new_description,
        new_responsible_person_id=new_responsible_person_id
    )


def delete_cost_by_id(id_: int):
    handle_session_error(CostAPI.delete_by_id, id_=id_)
