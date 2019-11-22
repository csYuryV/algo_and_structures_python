'''

20191122 Sikorskiy Yuriy
cs.yury.v@pm.me

6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.

'''

from random import randint

list_of_random_integers = [randint(-100, 100) for i in range(25)]

# list_of_random_integers = [1, 1, 1, 1, 1, 1]
# list_of_random_integers = [1, 1, 1, 1, 1, -5]
# list_of_random_integers = [1, 1, 1, -5, -5, -5]

minimum_value_index = list_of_random_integers.index(
    min(list_of_random_integers))
maximum_value_index = list_of_random_integers.index(
    max(list_of_random_integers))

begin_index, end_index = (
    maximum_value_index, minimum_value_index) if minimum_value_index > maximum_value_index else (
    minimum_value_index, maximum_value_index)

print(f'Список случайных целых чисел\n{list_of_random_integers}')
print(
    f'Элемент с минмамльным значением с индексом {minimum_value_index} равен {list_of_random_integers[minimum_value_index]}')
print(
    f'Элемент с максимальным значением с индексом {maximum_value_index} равен {list_of_random_integers[maximum_value_index]}')
# не включаю в список суммируемых элементов пограничные элементы с
# минимальным и максимальным значением
print(
    f'Суммам значений элементоврасположенных между элементами списка с минималным и максимальным значением {sum(list_of_random_integers[begin_index + 1:end_index])}')
