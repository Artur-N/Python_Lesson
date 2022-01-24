# 26. Возведите число А в натуральную степень B используя цикл

a = 2
b = 5

def Degree(a, b):
    for i in range(b):
        c = a*i
        return c #f'Число {a} в степени {i} = {a**i}')
print(Degree(a, b))


