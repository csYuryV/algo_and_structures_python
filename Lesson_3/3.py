'''

20191122 Sikorskiy Yuriy
cs.yury.v@pm.me

#3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.

'''

from random import randint

list_of_random_integers = [randint(-100, 100) for i in range(101)]

minimum_value_index = 0
maximum_value_index = 0

for i in range(1, 101):
    if list_of_random_integers[i] < list_of_random_integers[minimum_value_index]:
        minimum_value_index = i
    if list_of_random_integers[i] > list_of_random_integers[maximum_value_index]:
        maximum_value_index = i

print(f'Исходный список\n{list_of_random_integers}')
print(
    f'Элент списка с минимальным значением -> {list_of_random_integers[minimum_value_index]} с индексом {minimum_value_index}')
print(
    f'Элент списка с максимальным значением -> {list_of_random_integers[maximum_value_index]} с индексом {maximum_value_index}')
list_of_random_integers[minimum_value_index], list_of_random_integers[
    maximum_value_index] = list_of_random_integers[maximum_value_index], list_of_random_integers[minimum_value_index]

print(
    f'Список после смены местами минмального и максимального элементов списка\n{list_of_random_integers}')
