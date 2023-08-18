import keyboard
from time import sleep

from User import User
from State import State

from print_user_info import print_user_info


work = True
while work:
    if keyboard.is_pressed('q'):
        work = False
    elif keyboard.is_pressed('w'):
        print('Вам необходимо ввести данные о пользователе:')
        user_id = int(input('ID: '))
        user_name = input("Name: ")
        user_surname = input("Surname: ")
        user_phone = input("Phone: ")
        user_email = input("Email: ")
        State.save_user(User( 
            user_id,
            user_name,
            user_surname,
            user_phone,
            user_email
        ))
    
    print_user_info()
    print("\n\n\n\n\n")
    
    sleep(1 / 2)