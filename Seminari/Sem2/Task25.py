# 25. Найти сумму чисел от 1 до А

a = 5
def SummaNumbers(a):
    sum = 0
    for i in range(a+1):
        sum += i
    return sum
print(SummaNumbers(a)) 

