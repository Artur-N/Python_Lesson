# 11. Дано число из отрезка [10, 99]. Показать наибольшую цифру числа

n = 73
a = n // 10
b = n % 10
if a > b:
    print(a)
elif b > a:
    print(b)
else:
    print('Числа равны')
