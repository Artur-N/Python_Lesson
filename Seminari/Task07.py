# 7. Показать числа от -N до N

n = -1
if n >= 0:
    for i in range(-n, n+1):
        print(i)
else:
    for i in range(n, -n+1):
        print(i)

