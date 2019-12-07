"""
2019-12-06 Sikorskiy Yuriy
cs.yury.v@pm.me

1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).

"""
from random import randint
from timeit import timeit


def bubble_sorting(temp_list):
    for i in range(len(temp_list) - 1):
        for j in range(len(temp_list) - i - 1):
            if temp_list[j] < temp_list[j + 1]:
                temp = temp_list[j]
                temp_list[j] = temp_list[j + 1]
                temp_list[j + 1] = temp


def optimized_bubble_sorting(temp_list):
    n = len(temp_list) - 1
    for i in range(n):
        for j in range(n - i):
            j_plus_1 = j + 1
            if temp_list[j] < temp_list[j_plus_1]:
                temp_list[j], temp_list[j_plus_1] = temp_list[j_plus_1], temp_list[j]


def create_a_list_of_random_integers(
        min_value=-100,
        max_value=100,
        amount_of_numbers=100):
    return [randint(min_value, max_value) for _ in range(amount_of_numbers)]


if __name__ == '__main__':
    list_int = create_a_list_of_random_integers(amount_of_numbers=10000)
    print(list_int)
    temp_list = list_int.copy()
    setup_code = """
    from __main__ import optimized_bubble_sorting, temp_list
    """

    tm_optm_bs = timeit(
        'optimized_bubble_sorting(temp_list)',
        setup=setup_code,
        number=1)
    print(f'Время исполнения оптимизированного алгоритма: {tm_optm_bs} сек')
    # Время исполнения оптимизированного алгоритма: 4.8649735029976 сек
    print(temp_list)

    temp_list = list_int.copy()
    setup_code = """
    from __main__ import bubble_sorting, temp_list
    """
    tm_bs = timeit('bubble_sorting(temp_list)', setup=setup_code, number=1)
    print(f'Время исполнения неоптимизированного алгоритма: {tm_bs} сек.')
    # Время исполнения неоптимизированного алгоритма: 6.191245681999135 сек.
    print(temp_list)
