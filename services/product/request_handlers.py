from handlers.error_handlers.error_handlers import handle_session_error
from models.Product.ProductModule import ProductAPI


def create_product(name: str, description: str, price: int):
    handle_session_error(
        ProductAPI.create,
        name=name,
        description=description,
        price=price,
    )


def select_all_product():
    return handle_session_error(ProductAPI.read_all, False)


def select_product_by_id(ids: list[int]):
    return handle_session_error(ProductAPI.read_by_ids, False, ids=ids)


def update_product_by_id(
    id_: int,
    new_name: str | None,
    new_description: str | None,
    new_price: int | None
):
    handle_session_error(
        ProductAPI.update_by_id,
        id_=id_,
        new_name=new_name,
        new_description=new_description,
        new_price=new_price,
    )


def delete_product_by_id(id_: int):
    handle_session_error(ProductAPI.delete_by_id, id_=id_)
