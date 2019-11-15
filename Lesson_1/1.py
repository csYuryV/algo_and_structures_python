# 1.	Найти сумму и произведение цифр трехзначного числа,
# которое вводит пользователь.

'''

20191115 Sikorskiy Yuriy
cs.yury.v@pm.me

'''

try:
    num = int(input('Введите трехзначное целое положительное число <- '))

except ValueError:
    print('Некорректный ввод. Программа завершена')
    exit(-1)

if num < 100 or num > 999:
    print('Некорректный ввод. Программа завершена')
    exit(-2)

num100 = num//100
num10 = num%100//10
num1 = num%10

print(f'Сумма: {num100} + {num10} + {num1} = {num100 + num10 + num1}')
print(f'Произведение: {num100} * {num10} * {num1} = {num100 * num10 * num1}')

