from test.products import Product
from test.database import Database

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
        query = f"""DELETE FROM returned """
        delete = self.db.delete(query)
        print(delete)
        return delete

    def return_total(self, user_id, total_of_return):
        query = f"SELECT product_total FROM products where user_id = '{user_id}' AND id = '{total_of_return}'"
        total = self.db.fetchone(query)
        return 0 if not total else total[0]


    def return_products(self, user_id):
        query = f"SELECT * FROM products where user_id = '{user_id}'"
        user = self.db.fetchall(query)
        print(user)
        product_id = int(input('input product id'))
        total_of_return = int(input('input total of return'))
        if total_of_return <= self.return_total(user_id, total_of_return):
            query = f"""INSERT INTO returned (`product_id`, `total_of_return`)
                                      VALUES ('{product_id}', '{total_of_return}')
                                      """
            self.db.insert(query)
        else:
            print('wrong input')



returns = Returns()

returns.getall_returns()
#print(returns.return_total(3, 10))

#returns.return_products(3)
