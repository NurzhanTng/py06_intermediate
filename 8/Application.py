import json

from src.domain.User import User
from src.repository.UserRepository import UserRepository


repository = UserRepository()
user1 = User(
    'Nurzhan',
    'Tangatarov',
    '+77074862447',
    'a@mail.com',    
)

repository.append_data(
    repository.dto.UserToEntity(user1)
)