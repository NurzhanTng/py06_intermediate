from src.domain.Phone import Phone


class User:
    def __init__(self, id: int, name: str, surname: str, age: int, iin: str, phone: str, email: str) -> None:
        self.id = id
        self.name = name
        self.surname = surname
        self.age = age
        self.iin = iin
        self.phone = phone
        self.email = email

    def __str__(self) -> str:
        return f"class User:\n  self.id: {self.id},\n  self.name: {self.name},\n  self.surname: {self.surname},\n  self.age: {self.age},\n  self.iin: {self.iin},\n  self.phone: {self.phone},\n  self.email: {self.email}\n"