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


class WriteDB:
    """ Write a new user into the DB """
    def writeUser(self, name: str, surname: str, gender: str, cpf: str,
                  cel: str = '', birth: str = '', email: str = ''):
        with connectionTunnel() as connection:
            cursor = connection.cursor()
            sql = f'INSERT INTO {TABLE_NAME} ' \
                '(name, surname, gender, cpf, cel, birth, email) ' \
                'VALUES (?, ?, ?, ?, ?, ?, ?)'
            cursor.execute(sql, (str(name), str(surname), str(gender),
                                 str(cpf), str(cel), str(birth),
                                 str(email)))
            connection.commit()
            cursor.close()


class DeleteDB:
    """ Delete a user from the DB """
    @staticmethod
    def deleteUser(cpf):
        try:
            cpf = str(cpf)
        except ValueError:
            print("Error: id must be an integer")
            return

        with connectionTunnel() as connection:
            cursor = connection.cursor()
            cursor.execute(f'DELETE FROM {TABLE_NAME} WHERE cpf=?', (cpf,))
            connection.commit()
            cursor.close()


class EditDB:
    """ Edit an existing user in the DB """
    def editUser(self, user_id: int, name: str, surname: str, gender: str,
                 cpf: str, cel: str = '', birth: str = '',
                 email: str = ''):
        try:
            user_id = int(user_id)
        except ValueError:
            print("Error: id must be an integer")
            return

        with connectionTunnel() as connection:
            cursor = connection.cursor()
            sql = f'UPDATE {TABLE_NAME} '\
                'SET name=?, surname=?, gender=?, cpf=?, cel=?, ' \
                'birth=?, email=? WHERE id=?'
            cursor.execute(sql, (name, surname, gender, cpf,
                                 cel, birth, email, user_id))
            connection.commit()
            cursor.close()
