from handlers.error_handlers.error_handlers import handle_session_error
from models.BankAccount.BankAccountModule import BankAccountAPI


def create_bank_account(number: str, name: str):
    if len(number) != 16:
        raise Exception("number should have 16 digits")
    handle_session_error(BankAccountAPI.create, number=number, name=name)


def select_all_bank_accounts():
    return handle_session_error(BankAccountAPI.read_all, False)


def select_bank_accounts_by_id(id_: int):
    return handle_session_error(BankAccountAPI.read_by_id, False, id_=id_)


def update_bank_account_by_id(id_: int, new_number: str | None, new_name: str | None):
    return handle_session_error(BankAccountAPI.update_by_id, id_=id_, new_number=new_number, new_name=new_name)


def delete_bank_account_by_id(id_: int):
    return handle_session_error(BankAccountAPI.delete_by_id, id_=id_)
