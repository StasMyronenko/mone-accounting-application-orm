from config.db import Session

from models.BankAccount.BankAccountModule import BankAccountAPI
from models.BankAccount import data as bank_account_data

from models.Cost.CostModule import CostAPI
from models.Cost import data as cost_data

from models.Income.IncomeModule import IncomeAPI
from models.Income import data as income_data

from models.Personal.PersonalModule import PersonalAPI
from models.Personal import data as personal_data

from models.Product.ProductModule import ProductAPI
from models.Product import data as product_data

from models.Role.RoleModule import RoleAPI
from models.Role import data as role_data


def get_all_tables() -> dict[str: list]:
    with Session() as session:
        try:
            bank_accounts = BankAccountAPI.read_all(session)
            costs = CostAPI.read_all(session)
            incomes = IncomeAPI.read_all(session)
            personal = PersonalAPI.read_all(session)
            product = ProductAPI.read_all(session)
            role = RoleAPI.read_all(session)
            return {
                bank_account_data.tablename: bank_accounts,
                cost_data.tablename: costs,
                income_data.tablename: incomes,
                personal_data.tablename: personal,
                product_data.tablename: product,
                role_data.tablename: role
            }
        except Exception as e:
            print(e)
            return {}

