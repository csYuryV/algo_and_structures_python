'''
2019-12-12 Sikorskiy Yuriy
cv.yury.v@pm.me

2*. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.

'''
import hashlib

s = input("Введите строку из маленьких латинских букв: ")
r = set()

n = len(s)
for i in range(n):
    if i == 0:
        n = len(s) - 1
    else:
        n = len(s)
    for j in range(n, i, -1):
        print(s[i:j])
        r.add(hashlib.sha1(s[i:j].encode('utf-8')).hexdigest())

print(r)
print(f'Количество различных подстрок в строке {s} равно {len(r)}')

