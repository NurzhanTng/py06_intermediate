def zero_divizion(callback):
    def inner(x, y):
        if y == 0:
            raise ValueError('Нельзя делить на 0')
        else:
            callback(x, y)
    return inner


@zero_divizion
def divide(a, b):
    print(a / b)
    

divide(15, 3)