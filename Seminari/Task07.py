# 7. Показать числа от -N до N

n = -5
if n >= 0:
    for i in range(-n, n+1):
        print(i, end=' ')
else:
    for i in range(n, -n+1):
        print(i, end=' ')

print()

# Функция
def Show_numbers(N):
    if N >= 0:
        for i in range(-N, N+1):
            print(i, end=' ')
    else:
        for i in range(N, -N+1):
            print(i, end=' ')

Show_numbers(n)