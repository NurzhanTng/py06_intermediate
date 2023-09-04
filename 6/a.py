try:
    a = 105
    b = 2
    if b == 0:
        raise ZeroDivisionError('Второе число не должно быть нулем')
    if a > 1000 or b < 0:
        raise ValueError("Эти числа не подходят по требованию")
    print(a / b)
    print('a')
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
    print("Предоставьте подходящие значения")
else:
    print("Все прошло нормально")

print('b')