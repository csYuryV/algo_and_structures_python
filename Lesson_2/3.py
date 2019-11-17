"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.

20191116 Sikorskiy Yuriy
cs.yury.v@pm.me

"""

try:
    a = int(input('Введите натуральное число <- '))
except ValueError:
    print('Некорректный ввод. Программа завершена.')
    exit(-1)
if a <= 0:
    print('Некорректный ввод. Программа завершена.')
    exit(0)

i = a
a_out = 0
while i > 0:
    a_out *= 10
    digit = i % 10
    a_out += digit

    i = i // 10

print(f'{a} -> {a_out}')
