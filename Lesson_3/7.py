'''

20191122 Sikorskiy Yuriy
cs.yury.v@pm.me

7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.

'''

from random import randint

list_of_random_integers = [randint(-100, 100) for i in range(25)]

first_minimum_value = min(list_of_random_integers)
index_of_the_first_minimum_value = list_of_random_integers.index(
    first_minimum_value)
if list_of_random_integers.count(first_minimum_value) > 1:
    index_of_the_second_minimum_value = list_of_random_integers.index(
        first_minimum_value, index_of_the_first_minimum_value + 1)
else:
    second_minimum_value = min(list_of_random_integers[:index_of_the_first_minimum_value] +
                               list_of_random_integers[(index_of_the_first_minimum_value + 1):])
    index_of_the_second_minimum_value = list_of_random_integers.index(
        second_minimum_value)

print(f'Список случайных целых значений:\n{list_of_random_integers}')
print(
    f'Первое минимальное значение {list_of_random_integers[index_of_the_first_minimum_value]} с индексом {index_of_the_first_minimum_value}')
print(
    f'Второе минимальное значение {list_of_random_integers[index_of_the_second_minimum_value]} с индексом {index_of_the_second_minimum_value}')
