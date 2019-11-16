"""
4.	Написать программу, которая генерирует в указанных пользователем границах
●	случайное целое число,
●	случайное вещественное число,
●	случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f',
то вводятся эти символы. Программа должна вывести на экран любой
символ алфавита от 'a' до 'f' включительно.

20191115 Sikorskiy Yuriy
cs.yury.v@pm.me

"""
import random

print('Введите границы диапазона (min, max)')
try:
    mini = int(input('Введите целое число (min) <- '))
    maxi = int(input('Введите целое число (max) <- '))
except ValueError:
    print('Неккоректный ввод. Программа завершена.')
    exit(-1)

if mini > maxi:
    mini, maxi = maxi, mini
if mini == maxi:
    print('Некорректный ввод. Программа завершена.')
    exit(-1)

print(f'Случайное целое число в диапазоне от {mini} до {maxi} -> {int(random.random() * (maxi - mini + 1) + mini)}')
print(f'Случайное целое число в диапазоне от {mini} до {maxi} -> {random.random() * (maxi - mini) + mini:0.3f}')

print('\nВведите две строчные латинские буквы - начало и конец диапазона.')
symbol_begin = input('Введите букву начала диапазона <- ')
symbol_end = input('Введите букву конца диапазона <- ')

if len(symbol_begin) > 1 or len(symbol_end) > 1:
    print('Неккоректный ввод. Программа завершена.')
    exit(-2)

mini = ord(symbol_begin)
maxi = ord(symbol_end)
if mini < 97 or mini > 122 or maxi < 97 or maxi > 122:
    print('Неккоректный ввод. Программа завершена.')
    exit(-3)

if mini > maxi:
    mini, maxi = maxi, mini
if mini == maxi:
    print('Неккоректный ввод. Программа завершена.')
    exit(-1)

print(
    f'Случайный символ в диапазоне от {chr(mini)} до {chr(maxi)} -> {chr(int(random.random() * (maxi - mini + 1) + mini))}')
