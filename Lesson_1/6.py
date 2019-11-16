# 6.	Пользователь вводит номер буквы в алфавите. Определить, какая это буква.


'''

20191115 Sikorskiy Yuriy
cs.yury.v@pm.me

'''
import bpy, math

BEGINING_OF_ALPHABET = 97

try:
    id_symbol = int(input('Введите порядковый номер буквы в алфавите  <- '))
except ValueError:
    print('Некорректный ввод. Программа завершена.')
    exit(-1)

if id_symbol < 1 or id_symbol > 26:
    print('Некорректный ввод. Программа завершена.')
    exit(-2)

print(f'С порядковым номером {id_symbol} в алфавите буква \'{chr(BEGINING_OF_ALPHABET + id_symbol - 1)}\' ')
