from test.database import Database

class Discount:
    def __init__(self):
        self.db = Database()


    def getall_discounts(self):
        query = "SELECT * FROM discounts"
        products = self.db.fetchall(query)
        print(products)
        return products

    def discount(self, user_id):
        query = f"SELECT * FROM products where user_id = '{user_id}'"
        discount = self.db.fetchall(query)
        print(discount)
        if len(discount) != 0:
            query = f"SELECT sum(product_price * product_total) FROM products where user_id = '{user_id}'"
            total_price = self.db.fetchone(query)
            print(total_price)
            if total_price[0] >= 100000:
                return 0.9


    def save_discount(self, user_id):
        if self.discount_exist(user_id):
            print(f'User with user id {user_id} have discount.')
        else:
            if self.discount(user_id) == 0.9:
                query = f"""INSERT INTO discounts(`discount`, `user_id`)
                            VALUES ('{self.discount(user_id)}', '{user_id}')
                         """
                self.db.insert(query)


    def discount_exist(self, user_id):
        query = f"SELECT user_id FROM discounts where user_id = '{user_id}'"
        discounts = self.db.fetchone(query)
        return discounts if not discounts else discounts[0]


discount = Discount()

discount.getall_discounts()
