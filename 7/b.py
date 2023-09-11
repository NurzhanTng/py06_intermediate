# print(open('7/example.txt', 'r'))

import time

""" Взять весь текст из файла

# print('Hello')
# time.sleep(3)

f = open('7/example.txt', 'r')
content = f.read()
print(content)
"""


""" Полностью заменяет содержимое файла
f = open('7/example.txt', 'w')
f.write('Hello from python')
"""


""" Добавляет к содержимому файла строку
f = open('7/example.txt', 'a')
f.write('Hello from python')
"""


""" Важность закрытия файлов
f = open('7/example.txt', 'a')
f.write('Hello from python\n')

print(1)
sleep(2)
print(2)
f.close()
print(3)
"""

""" Возврат определенного количества символов
f = open('7/example.txt', 'r')
content = f.read(12)
print(content)
"""


""" Работа с получением данных из файла
f = open('7/example.txt', 'r')
# content = f.readline()
# print(content)

# for line in f:
#     print(line, end='')
    
lines = f.readlines()
print(lines[2])
"""


# with open('7/example.txt', 'r') as f:
#     for line in f:
#         print(line, end='')

# with open('7/new_file.txt', 'a', encoding='utf8') as f:
#     f.write('❤\n')
        
time.sleep(3)
