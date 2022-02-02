# Задать список из n чисел последовательности (1+1/n)^n и вывести на экран их сумму

n = 5
def Task16(a):
    list = []
    k = 0
    for i in range(1, a+1):
        r = (1+1/i)**i
        list.append(round(r, 2))
        k += r
    print(list)
    return round(k, 2)
print(Task16(n))


