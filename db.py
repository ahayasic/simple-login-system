import sqlite3


class DBManager:

    def __init__(self):
        self.__name = "login.db"
        self.__uri = f"file:{self.name}?mode=rw"

    @property
    def name(self):
        return self.__name

    @property
    def uri(self):
        return self.__uri

    def __is_db_available(self):
        try:
            conn = sqlite3.connect(self.uri, uri=True)
            conn.close()
            return True
        except sqlite3.OperationalError:
            return False

    def start_db(self):
        if self.__is_db_available():
            print("DB already exists. Using it")
        else:
            conn = sqlite3.connect(self.name)
            cursor = conn.cursor()

            cursor.execute("CREATE TABLE users (first_name TEXT, last_name TEXT, email TEXT, password TEXT)")

            conn.commit()
            conn.close()

    def query(self, query):
        conn = sqlite3.connect(self.name)
        cursor = conn.cursor()

        results = cursor.execute(query).fetchall()

        conn.commit()
        conn.close()

        return results

manager = DBManager()
