from src.service.MainService import MainService

import keyboard
import time


service = MainService()

while True:
    if keyboard.is_pressed('w'):
        new_user = service.create_new_user()
        print(new_user)
    if keyboard.is_pressed('q'):
        break
    
    print('.')
    time.sleep(0.5)