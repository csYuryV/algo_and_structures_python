'''

20191122 Sikorskiy Yuriy
cs.yury.v@pm.me

8.	Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.

'''

from random import randint

NUMBER_OF_LINES = 4
NUMBER_OF_COLUMNS = 5
list_user = []

for i in range(NUMBER_OF_LINES):
    list_line = []
    for j in range(NUMBER_OF_COLUMNS - 1):
        # while True:
        #     try:
        #         num = int(input(f'[{i}][{j}] <- '))
        #     except ValueError:
        #         print("Некорректный ввод. Пробуйте еще.")
        #         continue
        #     if num > 999 or num < 0:
        #         print('Введите целочисленное значение от 0 до 999.')
        #         continue
        #     break
        # list_line.append(num)
        list_line.append(randint(0, 999))
    list_line.append(sum(list_line))
    list_user.append(list_line)

for i in list_user:
    for index, value in enumerate(i):
        if index < NUMBER_OF_COLUMNS - 1:
            print(f'{value:4d}', end='')
        else:
            print(f'| {value:5d}')
