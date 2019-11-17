"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

20191117 Sikorskiy Yuriy
cs.yury.v@pm.me

"""

total = 0
while True:
    a = input('Введите число <- ')
    if a == '':
        break
    try:
        num = float(a)
    except ValueError:
        print('Некорректный ввод')
        continue

    total += num
    print(f'Сумма введенных чисел -> {total}')
