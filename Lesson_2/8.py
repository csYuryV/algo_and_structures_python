"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.

20191117 Sikorskiy Yuriy
cs.yury.v@pm.me

"""


def count_how_many_digits_in_number(number, digit):
    i = number
    number_of_digits = 0
    while i > 0:
        if i % 10 == digit:
            number_of_digits += 1
        i = i // 10
    return number_of_digits


try:
    number_of_input_numbers = int(input('Укажите количество вводимых чисел <- '))
    digit = int(input('Укажите цифру которую искать <- '))
except ValueError:
    print('Некорректный ввод. программа завершена')
    exit(-1)
if number_of_input_numbers <= 0 or digit < 0 or digit > 9:
    print('Некорректный ввод. программа завершена')
    exit(-2)
total_of_digits = 0
i = 1
while i <= number_of_input_numbers:
    try:
        number = int(input(f'{i}. Введите  число <- '))
    except ValueError:
        print('Некорректный ввод.')
        continue
    total_of_digits = total_of_digits + count_how_many_digits_in_number(number, digit)
    i += 1

print(f'Цифра {digit} была встречена {total_of_digits} раз(а)')
