from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from models.Base import Base
import models.IncomeProduct.data as data
import models.Income.data as income_data
import models.Product.data as product_data


class IncomeProduct(Base):
    __tablename__ = data.tablename

    id: Mapped[int] = mapped_column(data.id_, Integer, primary_key=True)
    income_id: Mapped[int] = mapped_column(data.income_id, ForeignKey(f'{income_data.tablename}.{income_data.id_}'))
    product_id: Mapped[int] = mapped_column(data.product_id, ForeignKey(f'{product_data.tablename}.{product_data.id_}'))
