import sqlite3
from shop_2.settings import db_name


class Database:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def close(self):
        self.cursor.close()
        self.connection.close()

    def execute(self, query):
        try:
            self.connect()
            self.cursor.execute(query)
        except Exception as e:
            print("Something went wrong - {0}".format(e))
            if self.connection:
                self.close()
            raise Exception

    def fetchall(self, query):
        self.execute(query)
        data = self.cursor.fetchall()
        self.close()
        return data

    def fetchone(self, query):
        self.execute(query)
        data = self.cursor.fetchone()
        self.close()
        return data

    def insert(self, query):
        self.execute(query)
        self.connection.commit()
        self.close()

