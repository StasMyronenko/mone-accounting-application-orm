from handlers.error_handlers.error_handlers import handle_session_error
from models.Income.IncomeModule import IncomeAPI
from models.Product.ProductModule import Product
from models.IncomeProduct.IncomeProductModule import IncomeProduct


def create_income(
    sum_: int,
    from_account: str,
    bank_account_id: int,
    products: list["Product"]
):
    if len(from_account) != 16:
        raise Exception('account number length should be 16 characters')
    handle_session_error(
        IncomeAPI.create,
        sum_=sum_,
        from_account=from_account,
        bank_account_id=bank_account_id,
        products=products
    )


def select_all_income():
    return handle_session_error(IncomeAPI.read_all, False)


def select_all_income_where_sum_less_than(max_sum: int):
    return handle_session_error(IncomeAPI.read_all_where_sum_less_than, False, max_sum=max_sum)


def update_income_by_id(
    id_: int,
    new_sum: int | None,
    new_from_account: str | None,
    new_bank_account_id: int | None,
    new_products: list["IncomeProduct"] | None,
):
    if len(new_from_account) != 16:
        raise Exception('account number length should be 16 characters')
    handle_session_error(
        IncomeAPI.update_by_id,
        id_=id_,
        new_sum=new_sum,
        new_from_account=new_from_account,
        new_bank_account_id=new_bank_account_id,
        new_products=new_products,
    )


def delete_income_by_id(id_: int):
    handle_session_error(IncomeAPI.delete_by_id, id_=id_)
