import time
import os
import shutil


# Данный скрипт работает, только если значения матрицы представляют собой один символ


# Узнаем размер матрицы в файле

# Считаем строчки
print('Started counting lines')
start_time_counting = time.time()
with open('matrix.txt', 'r') as matrix:
    lines = 0

    while True:
        string = matrix.read(5000000)
        if string:
            for symbol in string:
                if symbol == '\n':
                    lines += 1
                    print(f'Counted {lines} lines')
        else:
            break

# Считаем столбцы
print('Started counting columns')
with open('matrix.txt', 'r') as matrix:
    columns = 0

    flag = True
    while True:
        if flag:
            string = matrix.read(5000000)
            if string:
                list_of_symbols = list(string)
                try:
                    index = list_of_symbols.index('\n')
                    for position in range(index):
                        if list_of_symbols[position] == ' ':
                            columns += 1
                            print(f'Counted {columns} columns')
                    flag = False
                    break
                except ValueError:
                    columns += list.count(' ')
            else:
                flag = False
        else:
            break

end_time_counting = time.time()


print('Starting transposing')


# Очищаем файл, если он имеется
with open('t_matrix.txt', 'wb'):
    pass

start_time_transposing = time.time()

# Создаем буферный список, в который будем записывать по 5000000 символов
# и счетчик, который будет их считать
list_for_t_matrix = []
symbols_in_list = 0

# Отбираем числа с одинаковыми индексами по строкам, записываем в буферный список.
# Если буферный список переполняется, записываем значения в файл и очищаем список
with open('matrix.txt', 'r') as matrix:
    for column in range(columns):
        for line in range(lines):
            number = matrix.read(2)

            list_for_t_matrix.append(number)
            symbols_in_list += 2

            if symbols_in_list > 5000000:
                with open('t_matrix.txt', 'a+') as t_matrix:
                    t_matrix.write(''.join(list_for_t_matrix))
                list_for_t_matrix = []
                symbols_in_list = 0

            matrix.seek((columns * 2 + 2) * (line + 1) + column * 2)
            print(f'Transposing status: line "{line + 1}" from "{lines}", column "{column + 1}" from "{columns}"')

        list_for_t_matrix.append('\n')
        symbols_in_list += 1

        matrix.seek((column + 1) * 2)

# Записываем в файл остатки из буферного списка
with open('t_matrix.txt', 'a+') as t_matrix:
    t_matrix.write(''.join(list_for_t_matrix))

end_time_transposing = time.time()


print(f'There are {columns} columns and {lines} lines in origin matrix')
print(f'Counting took {round(end_time_counting - start_time_counting, 3)} seconds')
print(f'Transposing took {round(end_time_transposing - start_time_transposing, 3)} seconds')
