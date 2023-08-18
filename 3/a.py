class MyList:
    def __init__(self, arr:list) -> None:
        self.arr:list = arr
    
    def __add__(self, number):
        print('__add__ function')
        if type(number) != int:
            raise ValueError('Мы умеем работать только с числами!')
        self.arr.append(number)
        return self

    def __radd__(self, number):
        print('__radd__ function')
        return self.__add__(number)

    def __mul__(self, number):
        print('__mul__ function')
        if type(number) != int:
            raise ValueError('Мы умеем работать только с числами!')
        
        for i in range(len(self.arr)):
            self.arr[i] *= number
        
        return self
    
    def __str__(self) -> str:
        print('__str__ function')
        return str(self.arr)
        

a_example = MyList(list(range(3, 15, 2)))
# print(a_example.arr)
# print((a_example + 5).arr)
# print((5 + a_example).arr)
# print(a_example * 3)