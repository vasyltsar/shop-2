from shop_2.database import Database

db = Database()


queries = ["""CREATE TABLE IF NOT EXISTS users (
                     id integer primary key AUTOINCREMENT,
                     first_name text,
                     last_name text,
                     phone_number text UNIQUE,
                     city text,
                     FOREIGN KEY (id) REFERENCES products(user_id)
                    );""", """CREATE TABLE IF NOT EXISTS products (
                     id integer primary key AUTOINCREMENT,
                     product_type text,
                     product_price real,
                     product_total integer,
                     user_id integer NOT NULL 
                     
                    );"""]
for query in queries:
    db.execute(query)
