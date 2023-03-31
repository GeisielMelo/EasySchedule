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


class Appointment:
    """ Edit an existing user in the DB """
    def makeAppointment(self, name: str, cpf: str,
                        date: str, hour: str):
        with connectionTunnel() as connection:
            cursor = connection.cursor()
            sql = f'UPDATE {TABLE_NAME} ' \
                'SET appointment=?, date=?, hour=? ' \
                'WHERE name=? AND cpf=?'
            cursor.execute(sql, ('SIM', date, hour, name, cpf))
            connection.commit()
            cursor.close()

    def cancelAppointment(self):
        ...
