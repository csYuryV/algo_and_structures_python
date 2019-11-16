# 8.	Определить, является ли год, который ввел пользователем,
# високосным или не високосным.
#Год является високосным в двух случаях: либо он кратен 4,
# но при этом не кратен 100, либо кратен 400.

'''

20191116 Sikorskiy Yuriy
cs.yury.v@pm.me

По хорошему требуется уточнить условие задачи.



Так как высокосный год по юлианскому календарю (он же «старый стиль»,
по которому отмечается «Старый Новый год») тот, который кратен 4
(принятая длительность года 365.25 суток).
На заре становления юлианского календаря в 45г.до н.э. была большая путаница с
высокосными годами. Какой-то период они были каждый третий год, затем чтобы
выровнять накопившуюся ошибку высокосные года в течение какогото периода отменяли.

с 04.10.1582 г по инициативе папы римского Григория XIII в католических странах
в замен юлианскому календарю, был введен григорианский календарь, в котором принята
длительность года 365.2425 = 365 + 0.25 - 0.01 + 0.0025 = 365 + 1/4 - 1/100 + 1/400

Переход на "новый стиль" происходил не сразу.
Более того в странах, в которых господствовала православная христианская традиция
этому переходу намеренно противодействовали. Были попытки ввести в использование
новоюлианский  календарь(продолжительность года принята равной 365,242222 суток).
К примеру только в 1918 г. Советская Россия, точнее РСФСР
перешла на прменение григорианского календаря.

А еще таки есть иудейский календарь, по которому сегодня шаббат 18 хешвана 5780 г.
и все нормальные евреи в синагогах, слушают проповеди ребе, но это отдельная изТория.
Отмечу лишь, что в иудейском календаре усредненая длительность года принята равной
365.24677 суток.

'''

try:
    year = int(input('Введите номер года <- '))
except ValueError:
    print('Некорректный ввод. Программа завершена.')
    exit(-1)

if year < 0:
    print('Некорректный ввод. Программа завершена.')
    exit(0)

if year > 1582 and ((year%4 == 0 and  year%100 != 0) or year%400 == 0):
        print (f'{year} высокосный год ')
elif year <= 1582 and year % 4 == 0:
    print(f'{year} высокосный год ')
else:
    print(f'{year} невысокосный год ')





