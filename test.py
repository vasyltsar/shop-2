import json

class Database:
    def __init__(self, path_file):
        self.path_file = path_file

    def write(self, data):
        with open(self.path_file, 'w') as f:
            json.dump(data, f)

    def read(self):
        with open(self.path_file, 'r') as f:
            data = json.load(f)
            return data

class AddUser:
    def __init__(self, firs_name, last_name, phone_number, city):
        self.firs_name = firs_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.city = city
        self.db = Database(path_file='file.json')

    def lisl_user(self):
        return {'users':[]}

    def create_user(self):
        return {"first name": self.firs_name,
                "last name": self.last_name,
                "phone_number": self.phone_number,
                "city": self.city,
                "product": []}

    def save_user(self):
        data=self.db.read()
        data["users"].append(self.create_user())
        self.db.write(data)



class AddProduct:
    def __init__(self):
        self.db = Database(path_file='file.json')

    def add_product(self):
        data = self.db.read()
        users = data['users']
        if not users:
            print('sorry no user in database')
            exit(1)
        tries = 4
        while True:
            try:
                phone = int(input("Enter number: "))
                break
            except ValueError:
                if tries == 0:
                    print("you don't have any try!")
                    exit(1)
                print("not a number!")
                tries -= 1
                continue
        total = []
        total_cost = []
        for user in users:
            products = user['product']
            if phone == user['phone_number']:
                if not products:
                    products.append({
                        'type': input('type'),
                        'price': int(input('price')),
                        'total': int(input('total'))
                    })
                else:
                    for price in products:
                        total.append(price['total'])
                        total_cost.append(price['price'])
                        total_price = sum([x * y for x, y in zip(total_cost, total)])
                        if total_price >= 500000:
                            print('congratulations you have discount -10%')
                            discunt = int(input('price'))
                            discunt -= discunt*0.1
                            products.append({
                                'type': input('type'),
                                'price': discunt,
                                'total': int(input('total'))
                            })
                            break
                self.db.write(data)
                break
        else:
            print(phone, 'not in database, first you have to create user')
            exit(1)

add_product=AddProduct()
add_product.add_product()


#firs_name=input('input first name')
#last_name=input('input last name')
#phone_number=int(input('input phone number'))
#city=input('input city')
#
#user = AddUser(firs_name=firs_name,
#                last_name=last_name,
#                phone_number=phone_number,
#                city=city)
#
#user.save_user()
