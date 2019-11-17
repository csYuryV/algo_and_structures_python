"""
5.	Вывести на экран коды и символы таблицы ASCII, начиная с символа
под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

20191117 Sikorskiy Yuriy
cs.yury.v@pm.me

"""

BEGIN_KEY = 32
END_KEY = 127
j = 0
for i in range(BEGIN_KEY, END_KEY + 1):
    if ((i - BEGIN_KEY) % 10 == 0) and i != 32: print('\n')
    print(f'{i}:\'{chr(i)}\' ', end='')
