import sqlite3


class Db:
    def __enter__(self):
        return self

    def __init__(self, name="city.db"):
        self.connection = sqlite3.connect(f"./{name}")
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            """ SELECT count(name) FROM sqlite_master WHERE type='table' AND name='city' """
        )
        if not self.cursor.fetchone()[0] == 1:
            print("Создаём таблицу city...")
            sqlite_create_table_query = """ CREATE TABLE city (
                                            id INTEGER PRIMARY KEY,
                                            name TEXT NOT NULL); """

            self.cursor.execute(sqlite_create_table_query)
            self.connection.commit()
        else:
            print("Таблица city найдена")

    def add_city(self, city):
        self.cursor.execute("INSERT INTO city(name) VALUES(?)", [city])
        self.connection.commit()
        print(f"{city} успешно добавлен!")

    def add_cities(self, cities):
        self.cursor.executemany("INSERT INTO city(name) VALUES(?)", cities)
        self.connection.commit()
        print(f"{cities} успешно добавлены!")

    def get_city(self, id):
        self.cursor.execute("SELECT * FROM city WHERE id=(?)", (id,))
        return self.cursor.fetchone()

    def get_cities(self, ids):
        return [self.get_city(id) for id in ids]

    def get_all_cities(self, limit=None):
        self.cursor.execute("SELECT * FROM city")
        if not limit:
            return self.cursor.fetchall()
        else:
            return self.cursor.fetchmany(limit)

    def __exit__(self, ext_type, exc_value, traceback):
        self.cursor.close()
        if isinstance(exc_value, Exception):
            self.connection.rollback()
        else:
            self.connection.commit()
        self.connection.close()


with Db() as db:
    db.add_city("SPb")
    db.add_city("Tokyo")
    db.add_cities(
        [
            ("Moscow",),
            ("New York",),
            ("New Orlean",),
            ("Istambul",),
            ("Stockholm",),
            ("Berlin",),
            ("Hong-Kong",),
            ("Ottawa",),
        ]
    )
    print(db.get_city(1))
    print(db.get_city(6))
    print(db.get_cities([1, 2, 3, 8]))
    print(db.get_all_cities(5))
    print(db.get_all_cities())
