class Vector:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        return f"Координаты: ({self.x} | {self.y})"
    
    def __add__(self, vector):
        if type(vector) != Vector:
            raise ValueError('Векторы можно складывать только с векторами!')
        
        self.x += vector.x
        self.y += vector.y
        return self
               
    def __sub__(self, number): NotImplemented

    def __mul__(self, number):
        if type(number) != int:
            raise ValueError('Векторы можно умножать только на числа!')
        
        self.x *= number
        self.y *= number
        return self           
                
    def __truediv__(self, number): NotImplemented
    
    def __gt__(self, vector):
        if type(vector) != Vector:
            raise ValueError('Векторы можно сравнивать только с векторами!')
        
        distance1 = (self.x ** 2 + self.y ** 2) ** 0.5
        distance2 = (vector.x ** 2 + vector.y ** 2) ** 0.5
        return distance1 > distance2
        
    def __lt__(self, number): NotImplemented
    
    def __eq__(self, vector):
        if type(vector) != Vector:
            raise ValueError('Векторы можно сравнивать только с векторами!')
        
        return self.x == vector.x and self.y == self.y
        
    


# v1 = Vector(2, -1)
# v2 = Vector(3, 5)
# print(v1 + v2)
# print(v1 - v2)
# print(v1 * 3)
# print(v1 > v2)
# print(v1 == v2)