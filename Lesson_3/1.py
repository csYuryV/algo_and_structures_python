'''

20191122 Sikorskiy Yuriy
cs.yury.v@pm.me

1.	В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

'''


for i in range(2, 10):
    number_of_multiple_numbers = 0
    for j in range(2, 100):
        if j % i == 0:
            number_of_multiple_numbers += 1
    print(f'{i} -> {number_of_multiple_numbers}')
