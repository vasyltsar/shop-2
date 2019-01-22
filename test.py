import json

class Database:
    def __init__(self, path_file):
        self.path_file=path_file

    def write(self, data):
        with open(self.path_file, 'w') as f:
            json.dump(data, f)

    def read(self):
        with open(self.path_file, 'r') as f:
            data = json.load(f)
            return data

class AddUser:
    def __init__(self, firs_name, last_name, phone_number, city):
        self.firs_name=firs_name
        self.last_name=last_name
        self.phone_number=phone_number
        self.city=city
        self.db = Database(path_file='file.json')

    def lisl_user(self):
        return {'users':[]}

    def create_user(self):
        return {"first name":self.firs_name,
                "last name":self.last_name,
                "phone number":self.phone_number,
                "city":self.city,
                "product":[]}

    def save_user(self):
        data=self.db.read()
        data["users"].append(self.create_user())
        self.db.write(data)



class AddProduct:
    def __init__(self):
        self.db = Database(path_file='file.json')

    def add_product(self):
        data = self.db.read()
        users=data['users']
        if data['users'] == []:
            print('sorry no user in database')
            exit(1)
        phone=int(input('number'))
        phone_book=[]
        total=[]
        total_cost=[]
        for user in users:
            phone_book.append(user['phone number'])
            if phone in phone_book:
                for price in user['product']:
                    total.append(price['total'])
                    total_cost.append(price['price'])
                total_price=[x * y for x, y in zip(total_cost, total)]
                print(sum(total_price))
                if sum(total_price) <= 100000:
                    discount = int(input('price'))
                else:
                    print('you have -10proc')
                    discount = int(input('price'))
                    discount = discount - discount * 0.1
                user['product'].append({'type':input('type'),
                          'price':discount,
                          'total':int(input('total'))})
                self.db.write(data)
                break
        else:
            print('no user phone number', phone, 'first you have to create user')

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
































