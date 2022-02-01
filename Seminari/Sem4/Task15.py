# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]

n = 5

def MultiNum(a):
    list = []
    m = 1
    for i in range(1, a + 1):
        m *= i
        list.append(m)
    return list
print(MultiNum(n))
