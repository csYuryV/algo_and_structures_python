'''

20191122 Sikorskiy Yuriy
cs.yury.v@pm.me

#5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.

'''

from random import randint

list_of_random_integers = [randint(-100, 100) for i in range(10)]
print(f'Список слчайных целых чисел\n{list_of_random_integers}')

# Элегантно?
try:
    maximum_negative_value_index = list_of_random_integers.index(
        max([i for i in list_of_random_integers if i < 0]))
except ValueError:
    print('В списке нет элементов с отрицательным значением')
    exit(0)

print(
    f'Максимальное отрицательное значение у элемента с индексом {maximum_negative_value_index} равно {list_of_random_integers[maximum_negative_value_index]}')
