# here is function for running console application. If you want to run web or gui you need to change this file
from utils.db.show_all_tables import get_all_tables

start_text = 'Hello, here is my console application with db'
menu_text = """Choose one option(enter number):
0. Exit
1. Show all tables
"""


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


def run_console_application():
    print(start_text)
    while True:
        command_number = input(menu_text)
        match command_number:
            case '0':
                break
            case '1':
                show_all_tables()
    print('Good bye')
