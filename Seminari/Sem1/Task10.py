# 10. Показать вторую цифру трёхзначного числа

from random import randint

a = randint(100, 1000)
b = a // 10 % 10
print(a)
print(f'Вторая цифра числа {a} - {b}')

# Функция

def SecondNumber(a):
    return a // 10 % 10
print(a)
print(f'Вторая цифра числа {a} - {SecondNumber(a)}')