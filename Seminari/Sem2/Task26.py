# 26. Возведите число А в натуральную степень B используя цикл

a = 2
b = 5

def Degree(a, b):
    c = 1
    for i in range(b):
        c *= a
        print(c)
    return f'Число {a} в степени {b} = {c}'
print(Degree(a, b))

