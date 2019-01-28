from test.database import Database
from test.discounts import Discount


class Product:
    def __init__(self):
        self.db = Database()
        self.dis = Discount()


    def getall_products(self):
        query = "SELECT * FROM products"
        products = self.db.fetchall(query)
        print(products)
        return products


    def add_product(self, product_type, product_price, product_total, user_id):
        if self.dis.discount_exist(user_id) != None:
            x = 0.9
        else:
            x = 1
        print(self.dis.save_discount(user_id))
        query = f"""INSERT INTO products(`product_type`, `product_price`, `product_total`, `user_id`)
                          VALUES ('{product_type}', '{product_price * x}', '{product_total}', '{user_id}')
                                      """
        self.db.insert(query)





product = Product()


product.add_product('phone', 2500, 10, 1)

product.getall_products()
