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
        if self.dis.discount_exist(user_id) == user_id:
            discount = 0.9
        else:
            discount = 1
        self.dis.save_discount(user_id)
        query = f"""INSERT INTO products(`product_type`, `product_price`, `product_total`, `user_id`)
                          VALUES ('{product_type}', '{product_price * discount}', '{product_total}', '{user_id}')
                                      """
        self.db.insert(query)





product = Product()


product.add_product('glass', 250, 1, 3)

product.getall_products()
