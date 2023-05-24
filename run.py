# here is function for running console application. If you want to run web or gui you need to change this file
from services.bank_account.request_handlers import select_all_bank_accounts, create_bank_account, \
    update_bank_account_by_id, delete_bank_account_by_id
from services.cost.request_handlers import select_all_cost, create_cost, update_cost_by_id, delete_cost_by_id
from services.general.get_all_tables import get_all_tables
from services.income.request_handlers import select_all_income, create_income, update_income_by_id, \
    delete_income_by_id, select_all_income_where_sum_less_than
from services.personal.request_handlers import select_all_personal, create_personal, update_personal_by_id, \
    delete_personal_by_id, select_user_role, select_user_by_name
from services.product.request_handlers import select_all_product, select_product_by_id, create_product, \
    update_product_by_id, delete_product_by_id
from services.role.request_handlers import select_all_role, create_role, update_role_by_id, delete_role_by_id

start_text = 'Hello, here is my console application with db'
start_menu_text = """Choose one option(enter number):
0. Exit
1. Show all tables
2. Show table
3. Update table
4. Harder requests
"""

update_table_menu = '1. Create data\n2. Update data\n3. Delete data'

harder_request_menu = 'Choose action:\n1. Take user\'s role by his name\n2. Take all Incomes with products where sum less then'

table_list = ['BankAccount', 'Cost', 'Income', 'Personal', 'Product', 'Role']
table_dict = {}

for i in range(len(table_list)):
    table_dict[str(i)] = table_list[i]


def show_all_tables():
    res = get_all_tables()
    for table, values in res.items():
        print(f'table {table}: ')
        for element in values:
            attrs = vars(element)
            for key, value in attrs.items():
                if '_' in key[:2]:
                    continue
                else:
                    print(f'{key}: {value}', end=', ')
            print()
        print()


def show_attrs(data: list):
    for row in data:
        try:
            iter(data)
            for tuple_row in row:
                attrs = vars(tuple_row)
                for key, value in attrs.items():
                    if '_' not in key[:2]:
                        print(key, ': ', value, sep='')
        except TypeError:
            attrs = vars(row)
            for key, value in attrs.items():
                if '_' not in key[:2]:
                    print(key, ': ', value, sep='')
        print()


def run_console_application():
    print(start_text)
    while True:
        command_number = input(start_menu_text)
        match command_number:
            case '0':
                break
            case '1':
                show_all_tables()
            case '2':
                table_number = input(f'Choose table, {table_dict}')
                table = table_list[int(table_number)]
                match table:
                    case 'BankAccount':
                        data = select_all_bank_accounts()
                        show_attrs(data)
                    case 'Cost':
                        data = select_all_cost()
                        show_attrs(data)
                    case 'Income':
                        data = select_all_income()
                        show_attrs(data)
                    case 'Personal':
                        data = select_all_personal()
                        show_attrs(data)
                    case 'Product':
                        data = select_all_product()
                        show_attrs(data)
                    case 'Role':
                        data = select_all_role()
                        show_attrs(data)
            case '3':
                action_number = input(update_table_menu)
                table_number = input(f'Choose table, {table_dict}')
                table = table_list[int(table_number)]
                match action_number:
                    case '1':
                        match table:
                            case  'BankAccount':
                                number = input('Card number: ')
                                name = input('Card name')
                                create_bank_account(number, name)
                            case 'Cost':
                                sum_ = int(input('sum: '))
                                bank_account_id = int(input('bank_account_id: '))
                                to_account = input('to_account: ')
                                description = input('description: ')
                                responsible_person_id = int(input('responsible_person_id: '))
                                create_cost(sum_, bank_account_id, to_account, description, responsible_person_id)
                            case 'Income':
                                sum_ = int(input('sum_: '))
                                from_account = input('from_account: ')
                                bank_account_id = int(input('bank_account_id: '))
                                product_ids = list(map(
                                    lambda x: int(x), input('product_ids (separate it by space symbol): ').split(' ')
                                ))
                                products = select_product_by_id(product_ids)
                                create_income(sum_, from_account, bank_account_id, products)
                            case 'Personal':
                                name = input('name: ')
                                salary = int(input('salary: '))
                                role_id = int(input('role_id: '))
                                create_personal(name, salary, role_id)
                            case 'Product':
                                name = input('name: ')
                                description = input('description: ')
                                price = int(input('price: '))
                                create_product(name, description, price)
                            case 'Role':
                                role_name = input('role_name: ')
                                create_role(role_name)
                    case '2':
                        print('If you don\'t change smth just push Enter')
                        match table:
                            case 'BankAccount':
                                id_ = int(input('card id: '))
                                new_number = input('new card: ') or None
                                new_name = input('new card name') or None
                                update_bank_account_by_id(id_, new_number, new_name)
                            case 'Cost':
                                id_ = int(input('Cost id: '))
                                new_sum = int(input('new sum: ')) or None
                                new_bank_account_id = int(input('new_bank_account_id: ')) or None
                                new_to_account = input('new_to_account: ') or None
                                new_description = input('new_description: ') or None
                                new_responsible_person_id = int(input('new_responsible_person_id: ')) or None
                                update_cost_by_id(
                                    id_,
                                    new_sum,
                                    new_bank_account_id,
                                    new_to_account,
                                    new_description,
                                    new_responsible_person_id
                                )
                            case 'Income':
                                id_ = int(input('Income id: '))
                                new_sum = int(input('new_sum: ')) or None
                                new_from_account = input('new_from_account: ') or None
                                new_bank_account_id = int(input('new_bank_account_id: ')) or None
                                new_products_ids_str = input('new_product_ids (separate it by space symbol): ') or None
                                if new_products_ids_str:
                                    new_product_ids = list(map(
                                        lambda x: int(x), new_products_ids_str.split(' ')
                                    ))
                                    new_product = select_product_by_id(new_product_ids)
                                else:
                                    new_product = None
                                update_income_by_id(
                                    id_,
                                    new_sum,
                                    new_from_account,
                                    new_bank_account_id,
                                    new_product
                                )
                            case 'Personal':
                                id_ = int(input('id: '))
                                new_name = input('new_name: ') or None
                                new_salary = int(input('new_salary: ')) or None
                                new_role_id = int(input('new_role_id: ')) or None
                                update_personal_by_id(id_, new_name, new_salary, new_role_id)
                            case 'Product':
                                id_ = int(input('id: ')) or None
                                new_name = input('new_name: ') or None
                                new_description = input('new_description: ') or None
                                new_price = int(input('new_price: ')) or None
                                update_product_by_id(id_, new_name, new_description, new_price)
                            case 'Role':
                                id_ = int(input('id: '))
                                role_name = input('role_name: ') or None
                                update_role_by_id(id_, role_name)
                    case '3':
                        match table:
                            case 'BankAccount':
                                id_ = int(input('id: '))
                                delete_bank_account_by_id(id_)
                            case 'Cost':
                                id_ = int(input('id: '))
                                delete_cost_by_id(id_)
                            case 'Income':
                                id_ = int(input('id: '))
                                delete_income_by_id(id_)
                            case 'Personal':
                                id_ = int(input('id: '))
                                delete_personal_by_id(id_)
                            case 'Product':
                                id_ = int(input('id: '))
                                delete_product_by_id(id_)
                            case 'Role':
                                id_ = int(input('id: '))
                                delete_role_by_id(id_)
            case '4':
                action = input(harder_request_menu)
                match action:
                    case '1':
                        name = input('Write his name: ')
                        users = select_user_by_name(name)
                        for user in users:
                            role = select_user_role(user)
                            print(f'id: {user.id}, name: {user.name}, role: {role.role_name}')
                    case '2':
                        max_sum = int(input('Write max sum(integer number): '))
                        incomes = select_all_income_where_sum_less_than(max_sum)
                        for income in incomes:
                            products_name_list = []
                            for product in income.products:
                                products_name_list.append(product.name)
                            products_string = ', '.join(products_name_list)
                            print(f'id: {income.id}, sum: {income.sum}, products: {products_string}')
    print('Good bye')


def test_run():
    people = select_all_personal()
    user = people[0]
    role = select_user_role(user)
    print(role)

