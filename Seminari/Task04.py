# 4. Найти максимальное из трех чисел

a = 4
b = 5
c = 3
if c <= a >= b:
    print(f'Максимальное число {a}')
elif c <= b >= a:
    print(f'Максимальное число {b}')
else:
    print(f'Максимальное число {c}')

# Функция

def Max_of_3(a, b, c):
    if c <= a >= b:
        return a
    elif c <= b >= a:
        return b
    else:
        return c
print(Max_of_3(a, b, c))
