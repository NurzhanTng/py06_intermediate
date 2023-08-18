# def update_decorator(callback):
#     def inner(*args, **kwargs):
#         callback(*args, **kwargs)
#         Observer.notify()
#     return inner


class Observer:
    def __init__(self) -> None:
        self.state = "Nurzhan"
        self.listeners: list[callable] = []
    
    def subscribe(self, callback: callable):
        self.listeners.append(callback)
    
    def unsubscribe(self, callback: callable):
        self.listeners.remove(callback)
        
    def notify(self):
        for listener in self.listeners:
            listener(self.state)
    
    def update(self, name: str):
        self.state = name
        self.notify()
    

def text1(state):
    print(f'Здравствуйте, {state}')
    
def text2(state):
    print(f'Привет, {state}')






if __name__ == "__main__":
    observer = Observer()
    
    observer.subscribe(text1)
    
    observer.update('Aleksandr')
    
    observer.subscribe(text2)
    
    observer.update('Nurzhan')
