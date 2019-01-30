from test.database import Database

db = Database()

queries = ["""CREATE TABLE IF NOT EXISTS users (
                     id integer primary key AUTOINCREMENT,
                     type_of_purchase text,
                     first_name text,
                     last_name text,
                     phone_number text UNIQUE,
                     city text,
                     FOREIGN KEY (id) REFERENCES products(user_id),
                     FOREIGN KEY (id) REFERENCES discounts(user_id)
                    );""",
           """CREATE TABLE IF NOT EXISTS products (
                     id integer primary key AUTOINCREMENT,
                     product_type text,
                     product_price real,
                     product_total integer,
                     user_id integer NOT NULL 

                    );""",
           """CREATE TABLE IF NOT EXISTS discounts (
                     id integer primary key AUTOINCREMENT,
                     discount real,
                     user_id integer NOT NULL
                    );"""]
for query in queries:
    db.execute(query)
