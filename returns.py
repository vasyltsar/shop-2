from shop_2.products import Product
from shop_2.database import Database

class Returns:
    def __init__(self):
        self.db = Database()
        self.prod = Product()

    def getall_returns(self):
        query = "SELECT * FROM returned"
        returns = self.db.fetchall(query)
        print(returns)
        return returns


    def del_returned(self):
        query = f"""DELETE FROM returned where id = 1"""
        delete = self.db.delete(query)
        print(delete)
        return delete

    def available_total(self, product_id):
        query = f"SELECT product_total FROM products where id = '{product_id}'"
        total = self.db.fetchone(query)
        return 0 if not total else total[0]


    def return_products(self, user_id):
        query = f"SELECT id, product_type FROM products where user_id = '{user_id}'"
        products = self.db.fetchall(query)
        if not products:
            print('You dont have any products to return')
            exit(1)
        print('you have next product items:\n ' + '\n'.join(
            [f'type - {p[1]}, id - {p[0]}' for p in products]))
        product_id = int(input('input product id'))
        total_of_return = int(input('input total of return'))
        available_total = self.available_total(product_id)
        returned = self.get_returned(product_id)
        if not returned:
            if available_total < total_of_return:
                print('You cant return more than you bought')
                exit(1)
            self.save(product_id, total_of_return)
        else:
            going_to_return = returned + total_of_return
            if available_total < going_to_return:
                print('You cant return more than you bought')
                exit(1)
            self.update(product_id, going_to_return)

    def save(self, product_id, total_of_return):
        query = f"""INSERT INTO returned (`product_id`, `total_of_return`)
                    VALUES ('{product_id}', '{total_of_return}')
                 """
        self.db.insert(query)

    def update(self, product_id, going_to_return):
        query = f"""UPDATE returned SET total_of_return = '{going_to_return}' 
                    WHERE product_id = '{product_id}'                    
                 """
        self.db.insert(query)


    def get_returned(self, product_id):
        query = f"SELECT total_of_return FROM returned where product_id = '{product_id}'"
        total_of_return = self.db.fetchone(query)
        return total_of_return if not total_of_return else total_of_return[0]



returns = Returns()

returns.getall_returns()
#print(returns.return_total(3, 10))

returns.return_products(1)
#returns.save(3, 2)
