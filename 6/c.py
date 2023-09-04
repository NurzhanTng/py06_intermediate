from Exceptions.MyException import MyException

try:
    raise MyException('Hello from c.py')
except MyException as e:
    print(e)
