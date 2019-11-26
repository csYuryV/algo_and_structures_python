# -*- coding: utf-8 -*-
"""

20191123 Sikorskiy Yuriy
cs.yury.v@pm.me

1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

"""

from random import randint, random
import timeit, cProfile
import sys, os, json


def make_list1(i_min=-100, i_max=100, number_of_items=10):
    return [int(random() * (i_max - i_min + 1) + i_min - 1) for _ in range(number_of_items)]


def make_matrix1(i_min=-100, i_max=100, number_of_items=10):
    return [make_list1(i_min, i_max, number_of_items) for _ in range(number_of_items)]


def make_a_cubic_matrix1(i_min=-100, i_max=100, number_of_items=10):
    return [make_matrix1(i_min, i_max, number_of_items) for _ in range(number_of_items)]


def make_list2(i_min=-100, i_max=100, number_of_items=10):
    list_of_random_integers = list()
    for _ in range(number_of_items):
        list_of_random_integers.append(randint(i_min, i_max))
    return list_of_random_integers


def make_matrix2(i_min=-100, i_max=100, number_of_items=10):
    matrix_of_random_integers = list()
    for i in range(number_of_items):
        matrix_of_random_integers.append(make_list2(i_min, i_max, number_of_items))
    return matrix_of_random_integers


def make_a_cubic_matrix2(i_min=-100, i_max=100, number_of_items=10):
    cubic_matrix_of_random_integers = list()
    for i in range(number_of_items):
        cubic_matrix_of_random_integers.append(make_matrix2(i_min, i_max, number_of_items))
    return cubic_matrix_of_random_integers


def func_test_run(list_content, project_name, func_name, n_begin, n_end, n_step):
    old_stdout = sys.stdout
    res_test = dict()
    for i in range(n_begin, n_end, n_step):
        sdelta = '00' if i < 10 else ('0' if i < 100 else '')
        filename = f'{project_name}_{sdelta}{str(i)}.txt'
        print(f'{project_name} i = {i}, {filename}')

        sys.stdout = open(filename, 'w', encoding='utf-8')
        func_name_arg = f'{func_name}{i})'
        cProfile.run(func_name_arg)
        sys.stdout.close()
        sys.stdout = old_stdout
        with open(filename, 'r', encoding='utf-8') as fl:
           line = fl.readlines()[0]

           line = line.split()
        try:
            res_test[i] = {'func_call': int(line[0]), 'in_time': float(line[4])}
        except ValueError:
            pass
        os.remove(filename)
    list_content[project_name] = res_test


def main():
    s1 = """
def make_list1(i_min=-100, i_max=100, number_of_items=10):
    return [randint(i_min, i_max) for _ in range(number_of_items)]

make_list1(-100, 100, 100000)
"""

    s2 = """
def make_list2(i_min=-100, i_max=100, number_of_items=10):
    list_of_random_integers = list()
    for _ in range(number_of_items):
        list_of_random_integers.append(int(random() * (i_max - i_min + 1) + i_min - 1))
    return list_of_random_integers

make_list2(-100, 100, 100000)
"""

    s3 = """
randint(-100, 100)
"""

    s4 = """
int(random() * (100 - (-100) + 1) + (-100) - 1)
"""

    s5 = """
def make_list1(i_min=-100, i_max=100, number_of_items=10):
    return ['' for _ in range(number_of_items)]

make_list1(-100, 100, 100000)
"""

    s6 = """
def make_list2(i_min=-100, i_max=100, number_of_items=10):
    list_of_random_integers = list()
    for _ in range(number_of_items):
        list_of_random_integers.append('')
    return list_of_random_integers

make_list2(-100, 100, 100000)
"""

    s0 = """
def make_list3(i_min=-100, i_max=100, number_of_items=10):
    return [int(random() * (i_max - i_min + 1) + i_min - 1) for _ in range(number_of_items)]

make_list3(-100, 100, 100000)
"""

    # Совместное прменение генератора списков и генератра случайных чисел randint()
    print(timeit.timeit(s1, number=100, globals=globals()))
    # 7.311941235999257

    # Совместное применение традиционого цикла 'for in range', метода append и
    # генератора случайных чисел random
    print(timeit.timeit(s2, number=100, globals=globals()))
    # 2.3994159030007722
    # Результат лучше более чем в три раза (7.31/2,4 = 3,05 раза).

    # Начинаю вскрытие и сепарацию
    # Исследую генератор случайных чисел функцию randint()
    print(timeit.timeit(s3, number=10000000, globals=globals()))
    # 6.7208819719999155
    # Пожоже что randint() основной пожиратель машинного времени, но продолжу

    # Исследую генератор случайных чисел функцию random()с приведением
    # к целочисленному типу int
    print(timeit.timeit(s4, number=10000000, globals=globals()))
    # 1.5723754200007534
    # Результат лучше более чем в 4 раза(6.72/1.57 = 4.28 раза).

    # Продолжаю расчленение и вскрытие
    # Исследую генератор списков
    print(timeit.timeit(s5, number=100, globals=globals()))
    # 0.18098576700140256

    # Исследую традиционный цикл 'for in range' в сочетании с методом append()
    print(timeit.timeit(s6, number=100, globals=globals()))
    # 0.3623149770028249
    # Определенно генераторы списков быстрее в 2 раза(0.36/0.18 = 2)

    # Таким образом прихожу к выводу, что для создания списка случайных целых
    # значений наиболее целесообразно применять генератор списков в сочетании
    # с генератором случайных чисел int(random())

    # Проверяю выдвинутое предположение
    print(timeit.timeit(s0, number=100, globals=globals()))
    # 2.2138359890013817
    # Предположение подтверждается:  2.21 < 2.4 < 7.3

    # И тут Остапа понесло, не нравится мне копипаст, песочница какая-то.
    # Для чистоты эксперимента не могу задействовать мощь моих 16 потоков
    # Поэтому ковыляю на одном, прежде чем повторить у себя советую уменьшить N_END например до 100
    # При текущих настройках выполнение данного кода у меня занимало 6,33 мин.
    # Я исследую двойное вложение списков, тоесть кубоматрици (<- слово только что придумал)
    # со сторонами от 10 до 300 элементов(т.е 300**3 = 2.7e+7 целочисленных случайных значений)

    N_BEGIN = 10
    N_END = 301
    N_STEP = 10
    I_MIN = -100
    I_MAX = 100
    list_content = dict()
    func_test_run(list_content, 'lg1', f'make_list1({I_MIN}, {I_MAX}, ', N_BEGIN, N_END, N_STEP)
    func_test_run(list_content, 'lg2', f'make_matrix1({I_MIN}, {I_MAX}, ', N_BEGIN, N_END, N_STEP)
    func_test_run(list_content, 'lg3', f'make_a_cubic_matrix1({I_MIN}, {I_MAX}, ', N_BEGIN, N_END, N_STEP)
    func_test_run(list_content, 'll1', f'make_list2({I_MIN}, {I_MAX}, ', N_BEGIN, N_END, N_STEP)
    func_test_run(list_content, 'll2', f'make_matrix2({I_MIN}, {I_MAX}, ', N_BEGIN, N_END, N_STEP)
    func_test_run(list_content, 'll3', f'make_a_cubic_matrix2({I_MIN}, {I_MAX}, ', N_BEGIN, N_END, N_STEP)

    with open("res_file.json", "w") as write_file:
        json.dump(list_content, write_file)

    # в файле 1a.py реализован скрипт, который на основе полученных замеров времени отрисовывает графики затрат времени
    # для заполнения одномерного O(n), двумерного O(n**2) и трехмерного O(n**3) массивов, с количством элементов
    # по стороне от 10 до 300. Графики сохранены в файле lg123.png

if __name__ == '__main__':
    main()
