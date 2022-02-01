# Подсчитать сумму цифр в вещественном числе.

n = 123.456

def SumDigits(a):
    sum = 0
    for i in str(a):
        if i != '.':
            sum += int(i)
    return sum
print(SumDigits(n))

