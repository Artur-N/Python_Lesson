# 2. Найти максимальное из пяти чисел

a = [1, 3, 5, 4, 2]

def Max(a):
    max = 0
    for i in range(len(a)):
        if a[i] > max:
            max = a[i]
    return max
print(Max(a))


