from User import User


class State:
    __user__: User = None
        
    @classmethod
    def save_user(self, new_user: User):
        if type(User) != User:
            print('Функция может принимать только класс User')
        self.__user__ = new_user
    
    @classmethod
    def change_email(self, new_email):
        self.__user__.email = new_email
        
    @classmethod
    def get_user(self):
        return self.__user__