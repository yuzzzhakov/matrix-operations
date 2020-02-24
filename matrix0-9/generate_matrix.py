from random import randrange
import time
import os

# Алгоритм: генерируем блоки по 5 млн чисел, каждый из которых занимает
# 38.35 Мб оперативной памяти, и записываем блоки в файл

# import sys
# print(sys.getsizeof([randrange(10) for number in range(5000000)])/1024/1024, 'Mb')


# Очищаем файл, если он имеется
with open('matrix.txt', 'wb'):
    pass


# Задаем параметры матрицы
a = 10000
b = 10000

# В каком диапазионе генерируем числа (от 0 до r)
r = 10


# Сколько нужно сгенирировать случайных чисел
c = a * b
print(f'{c} numbers need to be generated')


# По сколько чисел генерируем в 1 блоке записи:
d = 5000000

# Сколько потребуется сгенерировать блоков записи по d чисел в каждом
whole = c // d

# Сколько останется чисел в последнем блоке
remainder = c % d

if remainder:
    blocks_number = whole + 1
else:
    blocks_number = whole

print(f'{blocks_number} blocks need to be generated')

if remainder:
    print(f'{remainder} numbers in last block')


print('Generating starts...')
start_time = time.time()

# Устанавливаем курсор position для отслеживания места переноса строки
position = 0

# Цикл для каждого сгенерированного целого блока записи (c // d)
for j in range(whole):
    list = []
    # Цикл для каждого сгенерированного числа в блоке
    for i in range(d):
        if position < a:
            list.append(str(randrange(r))+' ')
            position += 1
        else:
            list.append('\n')
            list.append(str(randrange(r)) + ' ')
            position = 1

    # Записываем список в строку
    string = ''.join(list)

    # Записываем блок в файл
    with open('matrix.txt', 'a+') as matrix:
        matrix.write(string)

    print(f'Generated block "{j+1}" from "{blocks_number}"')


list = []

if remainder:
    # Цикл для генерации оставшихся чисел (c % d)
    for k in range(remainder):
        if position < a:
            list.append(str(randrange(r)) + ' ')
            position += 1
        else:
            list.append('\n')
            list.append(str(randrange(r)) + ' ')
            position = 1

    string = ''.join(list)

    # Записываем оставшиеся числа
    with open('matrix.txt', 'a+') as matrix:
        matrix.write(string)
        matrix.write('\n')

    print(f'Generated block "{blocks_number}" from "{blocks_number}"')

else:
    with open('matrix.txt', 'a+') as matrix:
        matrix.write('\n')


print('The end of matrix generating')
print(f'Size of matrix.txt generated is {round(os.path.getsize("matrix.txt") / 1024 / 1024, 3)} Mb')
print(f'Generating took {round(time.time() - start_time, 3)} seconds')
