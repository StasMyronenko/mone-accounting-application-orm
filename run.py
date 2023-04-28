# here is function for running console application. If you want to run web or gui you need to change this file
from config.db import Session
from models.BankAccount.BankAccountModule import BankAccountAPI


def run_console_application():
    while True:
        pass


def simple_run():
    with Session() as session:
        res = BankAccountAPI.read_all(session)
        for element in res:
            print(element.number)
