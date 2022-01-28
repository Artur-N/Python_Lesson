# 29. Написать программу вычисления произведения чисел от 1 до N

n = 5
multi = 1 
for i in range(1, n+1):
    multi *= i
print(multi)

def Mult(a):
    m = 1
    for i in range(1, a+1):
        m *= i
    return m
print(Mult(n))