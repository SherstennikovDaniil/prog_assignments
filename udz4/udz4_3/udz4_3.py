import sqlite3


class Db:

    __tables = [
        [
            "tUsers",
            """ CREATE TABLE tUsers (
                id INTEGER PRIMARY KEY,
                userName TEXT NOT NULL,
                age INTEGER NOT NULL,
                gender TEXT NOT NULL); """,
        ],
        [
            "tPubl",
            """ CREATE TABLE tPubl (
                id INTEGER PRIMARY KEY,
                id_user INTEGER,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                FOREIGN KEY(id_user) REFERENCES tUsers(id)); """,
        ],
        [
            "tComments",
            """ CREATE TABLE tComments (
                id INTEGER PRIMARY KEY,
                textComm TEXT NOT NULL,
                id_Users INTEGER,
                id_Publ INTEGER,
                FOREIGN KEY(id_Publ) REFERENCES tPubl(id),
                FOREIGN KEY(id_Users) REFERENCES tUsers(id)); """,
        ],
    ]

    def __enter__(self):
        return self

    def __init__(self, name="publ.db"):
        self.connection = sqlite3.connect(f"./{name}")
        self.cursor = self.connection.cursor()
        for table in self.__tables:
            self.cursor.execute(
                f""" SELECT count(name) FROM sqlite_master WHERE type='table' AND name='{table[0]}' """
            )
            if not self.cursor.fetchone()[0] == 1:
                print(f"Создаём таблицу {table[0]}...")
                self.cursor.execute(table[1])
                self.connection.commit()
            else:
                print(f"Таблица {table[0]} найдена")

    def __exit__(self, ext_type, exc_value, traceback):
        self.cursor.close()
        if isinstance(exc_value, Exception):
            self.connection.rollback()
        else:
            self.connection.commit()
        self.connection.close()


with Db() as db:
    pass
