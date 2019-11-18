"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.

20191117 Sikorskiy Yuriy
cs.yury.v@pm.me

"""


def count_how_many_digits_in_number(number, digit):
    if number // 10 == 0:
        return 1 if number % 10 == digit else 0
    else:
        return 1 + count_how_many_digits_in_number(
            number // 10,
            digit) if number % 10 == digit else count_how_many_digits_in_number(
            number // 10,
            digit)


try:
    number_of_input_numbers = int(
        input('Укажите количество вводимых чисел <- '))
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
    total_of_digits = total_of_digits + \
        count_how_many_digits_in_number(number, digit)
    i += 1

print(f'Цифра {digit} была встречена {total_of_digits} раз(а)')
