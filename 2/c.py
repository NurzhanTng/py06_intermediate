class User:
    def __init__(self, id, name, surname, phone, email) -> None:
        self.id = id
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email


def null_value_check(callback):
    def inner(id, name, surname, phone, email):
        if id == None:
            raise ValueError('Айди не указано')
        elif name == '' or name == None:
            raise ValueError('Имя не указано')
        elif surname == '' or surname == None:
            raise ValueError('Фамилия не указано')
        elif phone == '' or phone == None:
            raise ValueError('Номер не указан')
        elif email == '' or email == None:
            raise ValueError('Почта не указана')
        else:
            return callback(id, name, surname, phone, email)
    
    return inner


user_list = []


@null_value_check
def create_user(id, name, surname, phone, email):
    user_list.append(User(id, name, surname, phone, email))
    

create_user(12, "Nurzhan", "Tangatarov", "+134241341", "nurzhan@gmail.com")

print(user_list)