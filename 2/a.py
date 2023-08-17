import random


class User:
    def __init__(self, name) -> None:
        self.name = name
        self.id = random.randint(0, 999999)
        
    def __str__(self) -> str:
        return f'Class User:\n  self.id: {self.id}\n  self.name: {self.name}\n'
    

class Customer(User):
    def __init__(self, name, goods_list) -> None:
        super().__init__(name)
        self.goods_list = goods_list
    
    def __str__(self) -> str:
        return f"{super().__str__()}  self.goods_list: {self.goods_list}\n"


class Admin(User):
    def __init__(self, name, customers) -> None:
        super().__init__(name)
        self.customers = customers
        
    def __str__(self) -> str:
        return f"{super().__str__()}  self.customers: {self.customers}"
    
    
        

    

u1 = User('Aleksandr')
c1 = Customer('Alisa', ['Adidas', 'Pensil'])
c2 = Customer('Dima', ['Apple', 'Pensil'])
c3 = Customer('Vanya', ['Adidas', 'Car'])

a1 = Admin('Vasilyi', [c1, c2, c3])



# print(u1)
# print(c1)
# print(a1)