# 28. Подсчитать сумму цифр в числе

a = int(input('Введите число: '))

def SumDigits(a):
    sum = 0
    while a != 0:
        sum += a % 10
        a = a // 10
    return sum
print(f'Сумма цифр числа {a} равна {SumDigits(a)}')

