import sqlite3
from contextlib import contextmanager
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_DIR = ROOT_DIR / 'data'
DB_NAME = 'db.sqlite3'
DB_FILE = DB_DIR / DB_NAME
TABLE_NAME = 'customers'


@contextmanager
def connectionTunnel():
    connection = sqlite3.connect(DB_FILE)
    try:
        yield connection
    finally:
        connection.close()


class SearchDB:
    @staticmethod
    def searchCPF(cpf):
        with connectionTunnel() as connection:
            cursor = connection.cursor()
            query = f"SELECT * FROM {TABLE_NAME} WHERE cpf = ?"
            cursor.execute(query, (cpf,))
            result = cursor.fetchone()
            return result is not None


