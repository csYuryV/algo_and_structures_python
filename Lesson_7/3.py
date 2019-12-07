"""

2019-12-07 Today is my birthday. Sikorskiy Yuriy
cs.yury.v@pm.me

3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
 который не рассматривался на уроках

"""

# Честно скажу, что я передрал код. Вместе с этим разобрался как он работает.
# Единственное с чем пришлось подебажится это рекурсивная функция top_key

import random
import statistics

# вариант 1
def median_square(x_list):
    for i in range(len(x_list)):
        smaller = equal = bigger = 0
        for j in range(len(x_list)):
            if x_list[i] < x_list[j]:
                smaller += 1
            elif x_list[i] > x_list[j]:
                bigger += 1
            else:
                equal += 1
        equal -= 1

        if smaller == bigger or smaller == equal + bigger or smaller + equal == bigger:
            return x_list[i]


# вариант 2
def partition(x_list, pivot):
    smaller = []
    equally = []
    bigger = []
    for item in x_list:
        if item < pivot:
            smaller.append(item)
        elif item > pivot:
            bigger.append(item)
        else:
            equally.append(item)
    return smaller, equally, bigger


def top_key(x_list, key):
    pivot = x_list[random.randrange(len(x_list))]
    left, middle, right = partition(x_list, pivot)

    if len(left) == key:
        return left
    if len(left) < key <= len(left) + len(middle):
        return middle
    if len(left) > key:
        return top_key(left, key)
    return top_key(right, key - len(left) - len(middle))


def median(x_list):
    result_list = top_key(x_list, len(x_list) // 2 + 1)
    return max(result_list)


SIZE = 5
LIMIT = 100
data = [random.randrange(0, LIMIT) for _ in range(2 * SIZE + 1)]
print(data)
print(f'mediana_square = {median_square(data)}')
print(data)
print(f'mediana = {median(data)}')
print(data)
print(sorted(data))

# вариант 3

print('*' * 50)
print(data)
print(f'mediana = {statistics.median(data)}')
print(sorted(data))