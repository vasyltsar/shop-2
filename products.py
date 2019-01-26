from shop_2.database import Database
from shop_2.discounts import Discount

class Product:
    def __init__(self):
        self.db = Database()
        self.dis = Discount()


    def getall(self):
        query = "SELECT * FROM products"
        products = self.db.fetchall(query)
        print(products)

    def add_product(self, product_type, product_price, product_total, user_id):
        if not self.dis.discount(user_id):
            product_price = product_price
        else:
            product_price = product_price * 0.9
        query = f"""INSERT INTO products(`product_type`, `product_price`, `product_total`, `user_id`)
                   VALUES ('{product_type}', '{product_price}', '{product_total}', '{user_id}')
                   """
        self.db.insert(query)


product = Product()

product.getall()
#product.add_product('tv', 10000, 1, 3)
#product.getall()




