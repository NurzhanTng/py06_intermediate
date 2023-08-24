from src.domain.User import User


class MainRepository:
    def __init__(self) -> None:
        self.users = []
        
    def save_user(self, new_user: User):
        self.users.append(new_user)