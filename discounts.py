from shop_2.database import Database

class Discount:
    def __init__(self):
        self.db = Database()

    def getall(self):
        query = "SELECT * FROM discounts"
        products = self.db.fetchall(query)
        return products

    def discount(self, user_id):
        query = f"SELECT sum(product_price * product_total) FROM products where user_id = '{user_id}'"
        total_price = self.db.fetchone(query)
        if total_price[0] >= 100000:
            print('Congratulations you have discount -10%')
            return 0.9


    def save_discount(self, user_id):
        if self.discount_exists(user_id):
            print(f'User with id {user_id} have discount.')
            exit(1)
        else:
            if self.discount(user_id) == 0.9:
                query = f"""INSERT INTO discounts(`discount`, `user_id`)
                                VALUES ('{self.discount(user_id)}', '{user_id}')
                             """
                self.db.insert(query)
            else:
                print("You don't have discount yet")


    def discount_exists(self, user_id):
        query = f"SELECT id FROM discounts where user_id = '{user_id}'"
        discount = self.db.fetchone(query)
        return discount if not discount else discount[0]


discount = Discount()
print(discount.getall())


