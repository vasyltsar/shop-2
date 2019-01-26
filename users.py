from shop_2.database import Database

class User:
    def __init__(self):
        self.db = Database()

    def getall(self):
        query = "SELECT * FROM users"
        users = self.db.fetchall(query)
        print(users)

    def add_user(self, first_name, last_name, phone_number, city):
        if self.user_exists(phone_number):
            print(f'Sorry user with phone number {phone_number} exists.')
            exit(1)
        query = f"""
        INSERT INTO users(`first_name`, `last_name`, `phone_number`, `city`)
        VALUES ('{first_name}', '{last_name}', '{phone_number}', '{city}')
        """
        self.db.insert(query)

    def user_exists(self, phone_number):
        query = f"SELECT id FROM users where phone_number = '{phone_number}'"
        user = self.db.fetchone(query)
        print(user)
        return user if not user else user[0]

user=User()

user.getall()
#user.add_user('petro', 'petrov', '063727492', 'odesa')
#user.getall()
#user.user_exists('0637274940')

