'''

2019-11-27 Sikorskiy Yuriy
cs.yury.v@pm.me

1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

'''

from collections import namedtuple

Quarters = namedtuple(
    'Quarters',
    'first_quarter second_quarter third_quarter fourth_quarter')
quarters = Quarters(
    'первый квартал',
    'второй квартал',
    'третий квартал',
    'четвертый квартал')


class Firm:
    def __init__(self, name):
        self._name = name
        self._profit = dict()
        self._total_profit = 0
        self._average_profit_for_year = 0

    def get_name(self):
        return self._name

    def get_profit(self):
        return self._profit

    def get_profit(self, key):
        return self._profit[key]

    def add_profit(self, key, value):
        self._profit[key] = value

    def get_average_profit_for_year(self):
        return self._average_profit_for_year

    def calc_average_profit_for_year(self):
        self._total_profit = sum(self._profit.values())
        self._average_profit_for_year = self._total_profit / 4
        return self._average_profit_for_year


class Firms:
    def __init__(self):
        self._list = list()
        self._total_profit = 0
        self._average_profit_for_year = 0

    def get_list(self):
        return self._list

    def add_firm(self, firm):
        self._list.append(firm)

    def calc_average_profit_for_year(self):
        self._average_profit_for_year = 0
        for firm in self._list:
            self._total_profit += firm.calc_average_profit_for_year()
        self._average_profit_for_year = self._total_profit / len(self._list)
        return self._average_profit_for_year

    def find_average_profit_lower(self):
        return [firm for firm in self._list if firm.get_average_profit_for_year(
        ) < self._average_profit_for_year]

    def find_average_profit_higher(self):
        return [firm for firm in self._list if firm.get_average_profit_for_year(
        ) > self._average_profit_for_year]


def input_n():
    MSG_ValueError = 'Необходимо ввести положительное целое число.'
    while True:
        try:
            n = int(input('Введите количество фирм: '))
            if n <= 0:
                print(MSG_ValueError)
                continue
            break
        except ValueError:
            print(MSG_ValueError)
            continue
    return n


def input_name_firm(i):
    return input(f'Введите имя фирмы номер {i + 1}: ')


def input_profit(j):
    MSG_ValueError = 'Необходимо ввести действительное число.'
    while True:
        try:
            n = float(input(f'Прибыль за {j}: '))
            break
        except ValueError:
            print(MSG_ValueError)
            continue
    return n


def main():
    n = input_n()
    firms = Firms()
    for i in range(n):
        firm = Firm(input_name_firm(i))

        for j in quarters:
            firm.add_profit(j, input_profit(j))
            pass

        firms.add_firm(firm)
    print(
        f'Средняя приыбыль за год для всех фирм составила: {firms.calc_average_profit_for_year():.2f}.')
    high_margin_firms = firms.find_average_profit_higher()
    low_margin_firms = firms.find_average_profit_lower()
    if len(low_margin_firms) == 0:
        print(f'Уникальная ситуция: среднегодовые прибыли всех фирм равны.')
    else:
        print(f'Список фирм, чья прибыль выше среднего:')
        for firm in high_margin_firms:
            print(f'{firm.get_name()} -> {firm.get_average_profit_for_year():.2f}.')

        print(f'Список фирм, чья прибыль ниже среднего:')
        for firm in low_margin_firms:
            print(f'{firm.get_name()} -> {firm.get_average_profit_for_year():.2f}.')


if __name__ == '__main__':
    main()
