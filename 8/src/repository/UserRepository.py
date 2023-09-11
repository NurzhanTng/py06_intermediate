import json

from src.domain.User import User
from src.dto.UserDto import UserDto


class UserRepository:
    def __init__(self) -> None:
        self.dto = UserDto()
    
    def __append_data(self, user: dict):
        try:
            data = []            
            with open('src/db/user.json', 'r', encoding='utf8') as f:
                content = f.read()
                if not content.strip() == '':
                    data = json.loads(content)            
            data.append(user)           
            
            with open('src/db/user.json', 'w', encoding='utf8') as f:
                f.write(json.dumps(data, indent=4))
        except Exception as e:
            print(e)
    
    def __get_data(self):
        try:
            data = []            
            with open('src/db/user.json', 'r', encoding='utf8') as f:
                content = f.read()
                if not content.strip() == '':
                    data = json.loads(content)      
            return data
        except Exception as e:
            print(e)
              
    def create_new_user(self, user: User): 
        self.__append_data(self.dto.UserToEntity(user))

    def get_user_by_id(self, id: int): 
        users:list[dict]=self.__get_data()
        for user in users:
            user=self.dto.EntityToUser(user)
            if user.id==id:
                return user
    
    def update_phone(self, id: int, phone: str): NotImplemented
    
    def update_password(self, id: int, password: str, new_password: str): NotImplemented
    
    def delete_user(self, id: int): NotImplemented