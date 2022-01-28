# 2. Найти максимальное из пяти чисел

import random

rndList = random.sample(range(0, 10), 5)
print(rndList)

def Max(a):
    max = 0
    for i in range(len(a)):
        if a[i] > max:
            max = a[i]
    return max
print(Max(rndList))


