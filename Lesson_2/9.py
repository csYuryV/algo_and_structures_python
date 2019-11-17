"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

20191117 Sikorskiy Yuriy
cs.yury.v@pm.me

"""


def calculate_the_sum_of_the_digits(number):
    total_sum_digit = 0
    i = number
    while i > 0:
        total_sum_digit += (i % 10)
        i = i // 10

    return total_sum_digit


number_with_maximum_digits = 0
maximum_sum_of_digits = 0
print('Для завершения ввода введите пустую строку')
while True:
    s_number = input('Введите натуральное число <- ')
    if s_number == '':
        break
    try:
        number = int(s_number)
    except ValueError:
        print('Некорректный ввод. программа завершена')
        exit(-1)
    if number < 0: number *= -1
    sum_of_digits = calculate_the_sum_of_the_digits(number)
    if sum_of_digits > maximum_sum_of_digits:
        maximum_sum_of_digits = sum_of_digits
        number_with_maximum_digits = number

print(f'Число {number_with_maximum_digits} содержит цифры, сумма которых максимальна и равна {maximum_sum_of_digits}')
