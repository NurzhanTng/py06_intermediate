from random import randint


class User:
    def __init__(self, name: str, surname: str, phone: str, email: str, id: int=randint(100_000, 999_999)) -> None:
        self.id = id
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email