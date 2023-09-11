from src.domain.User import User


class UserDto:
    def UserToEntity(self, user: User):
        return {
            'id': user.id,
            'name': user.name,
            'surname': user.surname,
            'phone': user.phone,
            'email': user.email,
        }
    
    def EntityToUser(self, user: dict):
        return User(
            id = user['id'],
            name = user['name'],
            surname = user['surname'],
            phone = user['phone'],
            email = user['email'],
        )