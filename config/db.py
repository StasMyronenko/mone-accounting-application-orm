from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mssql+pyodbc://SA:Admin123!@0.0.0.0:1433/AccountingMoneyWithORM?driver=ODBC+Driver+17+for+SQL+Server"

engine = create_engine(DATABASE_URL, echo=True)

Session = sessionmaker(engine)
