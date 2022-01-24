# 8. Показать четные числа от 1 до N

N = int(input('Введите число N: '))

for i in range(1, N+1):
    if i % 2 == 0:
        print(i, end=' ')
print()

# Функция

def Even(n):
    for i in range(1, n+1):
        if i % 2 == 0:
            print(i, end=' ')
Even(N)