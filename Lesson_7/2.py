"""

2019-12-06 Sikorskiy Yuriy
cs.yury.v@pm.me

2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

"""

from random import random


def create_a_list_of_random_float(
        min_value=0,
        max_value=50,
        amount_of_numbers=100):
    return [(min_value + random() * (max_value - min_value)) for _ in range(amount_of_numbers)]


def mixer(l, r):
    i = j = 0
    len_l = len(l)
    len_r = len(r)

    res = list()

    while i < len_l or j < len_r:
        if not i < len_l:
            res.append(r[j])
            j += 1
        elif not j < len_r:
            res.append(l[i])
            i += 1
        elif l[i] < r[j]:       # Именно Здесь происходит сортировка
            res.append(l[i])
            i += 1
        else:
            res.append(r[j])
            j += 1
    return res

# Я в восторге от простоты и совершенства этой рекурсивной дробилки.
# Понимаю, что вы имели ввиду когда говорили об элегантности  рекурсии
# Почемуто эта функция ассоцицруется у меня с образом двухствольной мясорубки
# пока разбирался как она работает заработал конкретный мигрень

def merge_sorting(temp_list):
    n = len(temp_list)
    if n < 2:
        return temp_list
    l = merge_sorting(temp_list[:n // 2])
    r = merge_sorting(temp_list[n // 2:n])

    return mixer(l, r)


if __name__ == '__main__':
    pass
    list_float = create_a_list_of_random_float(amount_of_numbers=10)
    print(list_float)

    res_list = merge_sorting(list_float)
    print(res_list)

