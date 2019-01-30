from shop_2.database import Database
from shop_2.discounts import Discount
from shop_2.users import User


class Product:
    def __init__(self):
        self.db = Database()
        self.dis = Discount()
        self.user = User()

    def getall_products(self):
        query = "SELECT * FROM products"
        products = self.db.fetchall(query)
        print(products)
        return products

    def add_product(self, product_type, product_price, product_total, user_id):
        if self.user.type_user_purchase(user_id) == 'retail':
            discount = self.dis.discount_exist(user_id)
            if not discount:
                result = self.dis.save_discount(user_id)
                discount = 1 if not result else result
        else:
            discount = 0.8
        query = f"""INSERT INTO products(`product_type`, `product_price`, `product_total`, `user_id`)
                      VALUES ('{product_type}', '{product_price * discount}', '{product_total}', '{user_id}')
                   """
        self.db.insert(query)

    def delete_product(self, product_type, user_id, product_total):
        query = f"""DELETE FROM products WHERE product_type = '{product_type}' AND user_id = '{user_id}' AND product_total = '{product_total}'"""
        delete = self.db.delete(query)
        print(delete)
        return delete



product = Product()


#product.add_product('phone', 1550, 5, 1)
#product.getall_products()
