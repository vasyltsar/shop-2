from shop_2.database import Database

class Discount:
    def __init__(self):
        self.db = Database()

    def total_cost(self, user_id):
        query = f"SELECT sum(product_price * product_total) FROM products where user_id = '{user_id}'"
        total_price = self.db.fetchone(query)
        print(total_price)
        if total_price[0] >= 100000:
            print('congratulations you have discount -10%')
            return 0.9
        else:
            return 1

    def getall(self):
        query = "SELECT * FROM discounts"
        products = self.db.fetchall(query)
        print(products)

    def discount(self, discount, user_id):
        query = f"""INSERT INTO discounts(`discount`, `user_id`)
                    VALUES ('{discount}', '{user_id}')
                 """
        self.db.insert(query)
