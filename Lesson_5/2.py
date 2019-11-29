'''



2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

'''
from collections import deque

dict_hex = {
    '0': 0x0,
    '1': 0x1,
    '2': 0x2,
    '3': 0x3,
    '4': 0x4,
    '5': 0x5,
    '6': 0x6,
    '7': 0x7,
    '8': 0x8,
    '9': 0x9,
    'A': 0xa,
    'B': 0xb,
    'C': 0xc,
    'D': 0xd,
    'E': 0xe,
    'F': 0xf}

list_hex = [
    '0',
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    'A',
    'B',
    'C',
    'D',
    'E',
    'F']
set_hex = set(list_hex)


# 16 ричные числа представлены в виде реверсированных колекций deque в которых более младшему разряду числа
# соответствует меньший индекс элемента колекции

def add_one_bit_hex(a, b):
    # к этой функции можно применитьтехнологию мемоизации с ипользованием двухмерного словаря
    # сложение одноразрядных 16-ричных числа
    total = dict_hex[a] + dict_hex[b]
    return deque([list_hex[total % 16], list_hex[total // 16]])


def add_zeros(a, number_of_zeros=1, side=0):
    # a колекция типа deque, side - указывает с какой стороны добавлять нули,
    # 0 - слева, 1 - справа
    zeros = ['0' for _ in range(number_of_zeros)]
    if side == 0:
        a.extendleft(zeros)
    if side == 1:
        a.extend(zeros)


def nonzero_high_bit(list_two_bit_numbers):
    for i in list_two_bit_numbers:
        if i[1] != '0':
            return True
    return False


def next_recount(list_two_bit_numbers):
    res = []
    res.append(deque([list_two_bit_numbers[0][0], list_hex[0]]))

    for i in range(1, len(list_two_bit_numbers)):
        res.append(add_one_bit_hex(
            list_two_bit_numbers[i - 1][1], list_two_bit_numbers[i][0]))
    if dict_hex[res[-1][1]] > 0:
        res.append(deque(['0', '0']))
    return res


def add_multi_bit_hex(a, b):
    # a, b - колекции типа deque

    delta_len = abs(len(a) - len(b))
    if delta_len > 0:
        if len(a) < len(b):
            add_zeros(a, delta_len, side=1)
        else:
            add_zeros(b, delta_len, side=1)
    ab = list(zip(a, b))
    res_bit_addition = []  # колекция промеуточных результатов побитового сложения разрядов
    for couple in ab:
        res_bit_addition.append(add_one_bit_hex(couple[0], couple[1]))
    res_bit_addition.append(deque(['0', '0']))
    # Проаеряю старшие биты если есть ненулевые сновы повторяю процедуру
    # побитового сложения со смещением

    if len(res_bit_addition) > 1:
        while nonzero_high_bit(res_bit_addition):
            res_bit_addition = next_recount(res_bit_addition)

    if len(res_bit_addition) == 1:
        result_add = deque(res_bit_addition)
    else:
        result_add = deque([i[0] for i in res_bit_addition])
        while result_add[-1] == '0' and len(result_add) > 1:
            result_add.pop()
        return result_add


def multiply_one_bit_hex(a, b):
    # к этой функции можно применитьтехнологию мемоизации с ипользованием двухмерного словаря
    # умножение одноразрядных 16-ричных числа
    total = dict_hex[a] * dict_hex[b]
    return deque([list_hex[total % 16], list_hex[total // 16]])


def multiply_multi_bit_hex(a, b):
    res = []
    for i in range(len(a)):
        for j in range(len(b)):
            number_of_zeros = i + j
            res_multiply_one_bit_hex = multiply_one_bit_hex(a[i], b[j])
            if number_of_zeros > 0:
                add_zeros(res_multiply_one_bit_hex, number_of_zeros)
            res.append(res_multiply_one_bit_hex)
    if len(res) == 1:
        if res[0][1] == '0':
            res[0].pop()
        return res[0]
    if len(res) >= 2:
        res_multiply = add_multi_bit_hex(res[0], res[1])
    if len(res) > 2:
        for i in range(2, len(res)):
            res_multiply = add_multi_bit_hex(res_multiply, res[i])
    return res_multiply


def input_hex(invitation):
    MSG_ValueError = 'Некорректный ввод.'
    correct_input = False
    while not correct_input:
        h = input(invitation).upper()
        h_list = deque(list(h))
        correct_input = True
        for i in h_list:
            if i not in set_hex:
                print(MSG_ValueError)
                correct_input = False
                break
    h_list.reverse()
    return h_list


def main():
    print('Введите два шестнадцатиричных числа.')
    a = input_hex('Введите первое шестнадцатиричное число: ')
    b = input_hex('Введите второе шестнадцатиричное число: ')

    res = add_multi_bit_hex(a, b)
    res1 = multiply_multi_bit_hex(a, b)
    a.reverse()
    b.reverse()
    res.reverse()
    res1.reverse()
    print(f'{a} + {b} = {res}')
    print(f'{a} * {b} = {res1}')


if __name__ == '__main__':
    main()
