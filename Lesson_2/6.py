"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

20191117 Sikorskiy Yuriy
cs.yury.v@pm.me

"""

import random


def a(num, i):
    if i == 0:
        print(print(
            f'Вы не отгадали число за 10 попыток(хотя достаточно 7 попыток).\nБыло загадано число: {num}'))
        exit(0)
    else:
        while True:
            try:
                num_from_user = int(input('(0...100) <- '))
            except ValueError:
                print('Некорректный ввод.')
                continue
            if num_from_user < 0 or num_from_user > 100:
                print('Некорректный ввод.')
                continue
            break
        if num == num_from_user:
            print('Вы отгадали число')
            exit(0)
        elif num < num_from_user:
            print('Загаданное число меньше')
        else:
            print('Загаданное число больше')
        a(num, i - 1)

a(random.randint(0, 100), 10)
