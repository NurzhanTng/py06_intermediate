from State import State


def print_user_info():
    user = State.get_user()
    if user is None:
        return
    print(f'Здравствуйте, {user.name}')