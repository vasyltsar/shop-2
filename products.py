from shop_2.database import Database

class Product:
    def __init__(self):
        self.db = Database()

    def getall(self):
        query = "SELECT * FROM products"
        products = self.db.fetchall(query)
        print(products)

    def add_product(self, product_type, product_price, product_total, user_id):
        query = f"""INSERT INTO products(`product_type`, `product_price`, `product_total`, `user_id`)
                   VALUES ('{product_type}', '{product_price}', '{product_total}', '{user_id}')
                   """
        self.db.insert(query)



product=Product()

product.getall()
#product.add_product('tv', 10000, 1, 1)
#product.getall()


