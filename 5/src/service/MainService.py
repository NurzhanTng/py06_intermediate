from src.domain.User import User

from src.repository.MainRepository import MainRepository


class MainService:
    def __init__(self) -> None:
        self.repository = MainRepository()
    
    
    def create_new_user(self) -> User:
        """
        Function to create new user
        """
        id = int(input(""))
        name = input("")
        surname = input("")
        age = int(input(""))
        iin = input("")
        phone = input("")
        email = input("")
        
        new_user = User(id, name, surname, age, iin, phone, email)
        self.repository.save_user(new_user)
        return new_user