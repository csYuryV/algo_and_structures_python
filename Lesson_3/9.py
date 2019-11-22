'''

20191122 Sikorskiy Yuriy
cs.yury.v@pm.me

# 9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы.

'''

from random import random
from random import randint

NUMBER_OF_LINES = 4
NUMBER_OF_COLUMNS = 5

list_user = []
for i in range(NUMBER_OF_LINES):
    list_line = []
    for j in range(NUMBER_OF_COLUMNS):
        # list_line.append(randint(0, 999))
        list_line.append(int(random() * 1000))
    list_user.append(list_line)

list_of_minimum_values_in_columns = list_user[0].copy()

for i in list_user[1:]:
    for j in range(len(i)):
        if i[j] < list_of_minimum_values_in_columns[j]:
            list_of_minimum_values_in_columns[j] = i[j]

for i in list_user:
    for index, value in enumerate(i):
        print(f'{value:4d}', end='')
    print()

print(
    f'\nМаксимальный элемент среди минимальных элементов столбцов: {max(list_of_minimum_values_in_columns)}')
