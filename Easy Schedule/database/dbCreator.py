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


class CreateDB:
    """ Create a new DB archive"""
    def makeDataFolder(self):
        if not DB_DIR.exists():
            DB_DIR.mkdir(parents=True, exist_ok=True)

    def makeDataBase(self):
        with connectionTunnel() as connection:
            cursor = connection.cursor()

            cursor.execute(
                f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
                '('
                'id INTEGER PRIMARY KEY AUTOINCREMENT,'
                'name TEXT,'
                'surname TEXT,'
                'cpf TEXT,'
                'birth TEXT,'
                'gender TEXT,'
                'appointment TEXT,'
                'date TEXT,'
                'hour TEXT,'
                'cel TEXT,'
                'email TEXT'
                ')'
            )
            connection.commit()
            cursor.close()
