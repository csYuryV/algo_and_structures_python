# -*- coding: utf-8 -*-

'''

20191126 Sikorskiy Yuriy
cs.yury.v@pm.me

2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»

'''

import timeit
import matplotlib.pyplot as plt


# Алгоритм реализации: решето Эратосфена:
def apply_the_eratosthenes_method(n):
    a = list(range(n + 1))
    a[1] = 0
    lst = []
    i = 2
    while i <= n:
        if a[i] != 0:
            lst.append(a[i])
            for j in range(i, n + 1, i):
                a[j] = 0
        i += 1
    return lst


# Алгоритм реализации: решето Сундарама:
def apply_the_sundarama_method(n):
    D = n // 2
    B = n // 6
    m = set(range(D))
    for i in range(1, B + 1):
        for j in range(i, (D + i) // (1 + 2 * i) + 1):
            m.discard(i + j + 2 * i * j)
    lst = [2 * x + 1 for x in m]
    return lst


def draw_plt(x, y_er, y_su, delta):
    fig = plt.figure(figsize=plt.figaspect(0.75))
    ax = fig.add_subplot(111)

    # ax.plot(x, y_er, color='lightblue', linewidth=3)
    ax.plot(x, y_su, color='lightblue', linewidth=1)
    ax.plot(x, y_er, color='blue', linewidth=1)
    ax.plot(x, delta, color='red', linewidth=1)
    plt.savefig('2_resheto.png')
    plt.show()


def main():
    N_BEGIN = 10
    N_END = 400000
    N_STEP = 2000

    x = []
    y_er = []
    y_su = []
    delta = []

    for i in range(N_BEGIN, N_END, N_STEP):
        time_er = timeit.timeit(
            f'apply_the_eratosthenes_method({i})',
            number=10,
            globals=globals())
        time_su = timeit.timeit(
            f'apply_the_sundarama_method({i})',
            number=10,
            globals=globals())
        x.append(i)
        y_er.append(time_er)
        y_su.append(time_su)
        d = (time_su - time_er)
        delta.append(d * 4)
        print(f'i = {i:5d}, Er -> {time_er:.5f} Su -> {time_su:.5f} delta -> {d:.5f}')

    draw_plt(x, y_er, y_su, delta)


if __name__ == "__main__":
    main()

# Очевидно, что скорость исполнения алгоритма Сундарама (голубая линия) для значений n от 0 до 17000 више.
# выраженный провал в скорости исполнения для n больших 320000
# При значениях n больше 17000 болле быстрым становится алгоритм Эрастафена (синяя линия графика).
# Красным графиком демострируется разность между временем выполнения алгоритмов Сундарама и Эрастофена
