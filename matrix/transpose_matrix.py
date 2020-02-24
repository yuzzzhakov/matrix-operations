import time
import os
import shutil


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

# Создаем временную папку для файлов
path = os.getcwd() + '\\tempfiles'
os.mkdir(path)


start_time_transposing = time.time()
with open('matrix.txt', 'r') as matrix:

    # Создаем во временной папке файл для каждой колонки
    for column in range(columns):
        with open(path + f'/col{column}.txt', 'a+') as file:
            print(f'Stage "1" from "3". Tempfile "{column + 1}" from "{columns}" created')
            pass

    # Каждое число матрицы записываем в свой файл колонки
    for line in range(lines):
        for column in range(columns):
            number = ''
            while True:
                symbol = matrix.read(1)
                if symbol != ' ':
                    number += symbol
                else:
                    break

            with open(path + f'/col{column}.txt', 'a+') as file:
                file.write(f'{number + " "}')

        matrix.read(1)
        print(f'Stage "2" from "3". Numbers from line "{line + 1}" are written. There are "{lines}" lines at all')

    # Добавляем по переносу строки в каждый временный файл
    for column in range(columns):
        with open(path + f'/col{column}.txt', 'a+') as file:
            file.write('\n')

# Создаем файл транспонированной матрицы и собираем ее из временных файлов
with open('t_matrix.txt', 'a+') as t_matrix:
    for column in range(columns):
        with open(path + f'/col{column}.txt', 'r') as file:
            flag = True
            while True:
                if flag:
                    string = file.read(5000000)
                    if string:
                        t_matrix.write(string)
                    else:
                        flag = False
                else:
                    break
        print(f'Stage "3" from "3". Collected "{column + 1}" column from "{columns}" in transposed matrix')

end_time_transposing = time.time()


# Вычисляем размер удаляемой временной папки
size = 0
for dirpath, dirnames, filenames in os.walk(path):
    for f in filenames:
        fp = os.path.join(dirpath, f)
        size += os.path.getsize(fp)



# Удаление временной папки с файлами
shutil.rmtree(path)

print(f'There are {columns} columns and {lines} lines in matrix')
print(f'Counting took {round(end_time_counting - start_time_counting, 3)} seconds')
print(f'Transposing took {round(end_time_transposing - start_time_transposing, 3)} seconds')
print(f'Temporary files had been taken {round(size / 1024 / 1024, 3)} Mb')
