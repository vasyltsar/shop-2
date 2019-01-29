from test.database import Database

class User:
    def __init__(self):
        self.db = Database()

    def getall_users(self):
        query = "SELECT * FROM users"
        users = self.db.fetchall(query)
        print(users)


    def add_user(self, type_of_purchase, first_name, last_name, phone_number, city):
        if self.user_exists(phone_number):
            print(f'Sorry user with phone number {phone_number} exists.')
            exit(1)
        query = f"""
        INSERT INTO users(`type_of_purchase`, `first_name`, `last_name`, `phone_number`, `city`)
        VALUES ('{type_of_purchase}', '{first_name}', '{last_name}', '{phone_number}', '{city}')
        """
        self.db.insert(query)

    def user_exists(self, phone_number):
        query = f"SELECT id FROM users where phone_number = '{phone_number}'"
        user = self.db.fetchone(query)
        print(user)
        return user if not user else user[0]

    def type_user_purchase(self, id):
        query = f"SELECT type_of_purchase FROM users where id = '{id}'"
        purchase = self.db.fetchone(query)
        return purchase if not purchase else purchase[0]

user=User()

#  wholesale_or_retail
#user.add_user('retail', 'petro', 'petrov', '0637274942', 'odesa')

user.getall_users()

print(user.type_user_purchase(3))