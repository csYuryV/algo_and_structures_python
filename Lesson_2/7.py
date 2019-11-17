"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

20191117 Sikorskiy Yuriy
cs.yury.v@pm.me

"""
from threading import Thread


class Verification_of_the_statement:
    def __init__(self):
        self._i = 1
        self._total = 1
        self._val = 1
        self._keep_checking = True
        self._the_truth_of_the_statement = True

    def __call__(self):
        return self._the_truth_of_the_statement

    def get_i(self):
        return self._i

    def get_total(self):
        return self._total

    def stop_check(self):
        self._keep_checking = False

    def loop(self):
        while self._keep_checking:
            self._val = self._i * (self._i + 1) // 2
            if self._total != self._val:
                print('Проверка утверждения завершена. Утверждение не верно.')
                self._the_truth_of_the_statement = False
                self._keep_checking = False

            self._i += 1
            self._total += self._i

    def __str__(self):
        return f'n = {self._i}, 1+2+...+n = {self._total}, n(n+1)/2 = {self._val}'


verification_of_the_statement = Verification_of_the_statement()

verif_loop = Thread(target=verification_of_the_statement.loop)
verif_loop.start()

print('Введите \'1\', чтобы узнать состояние проверки, или \'0\' для завершения проверки')
while True:
    key_user = input('<- ')
    if key_user == '0':
        verification_of_the_statement.stop_check()
        break
    if key_user == '1':
        if verification_of_the_statement():
            print(f'Равенство истино, {str(verification_of_the_statement)}')
        else:
            print(f'Равенство ложно для {str(verification_of_the_statement)}')
            exit(0)
verif_loop.join()

if verification_of_the_statement():
    print(
        f'Равенство истинно для всех значений n = (1, ..., {verification_of_the_statement.get_i()})')
else:
    print(f'Равенство ложно для {str(verification_of_the_statement)}')
