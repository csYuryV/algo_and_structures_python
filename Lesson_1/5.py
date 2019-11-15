#5.	Пользователь вводит две буквы. Определить, на каких местах
# алфавита они стоят, и сколько между ними находится букв.

'''

20191115 Sikorskiy Yuriy
cs.yury.v@pm.me

'''

BEGINING_OF_ALPHABET = 97

print('\nВведите две строчные латинские буквы:.')
symbol1 = input('Введите первую букву <- ')
symbol2 = input('Введите вторую букву <- ')

if len(symbol1) > 1 or len(symbol2) > 1:
    print('Неккоректный ввод. Программа завершена.')
    exit(-2)

id_symbol1 = ord(symbol1)
id_symbol2 = ord(symbol2)
if id_symbol1 < 97 or id_symbol1 > 122 or id_symbol2 < 97 or id_symbol2 > 122:
    print('Неккоректный ввод. Программа завершена.')
    exit(-3)

if id_symbol1 > id_symbol2:
    id_symbol1, id_symbol2 = id_symbol2, id_symbol1
    symbol1, symbol2 = symbol2, symbol1
if id_symbol1 == id_symbol2:
    print('Неккоректный ввод. Программа завершена.')
    exit(-1)

print(f'Символ \'{symbol1}\' находится на {id_symbol1 - BEGINING_OF_ALPHABET} месте (нумерация начинается с нуля).')
print(f'Символ \'{symbol2}\' находится на {id_symbol2 - BEGINING_OF_ALPHABET} месте (нумерация начинается с нуля).')

delta = id_symbol2 - id_symbol1 - 1

print(f'Между \'{symbol1}\' и \'{symbol2}\' находится {delta} букв(а,ы).')
