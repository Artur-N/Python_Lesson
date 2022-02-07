# Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов. 
# Т е для k = 8, список будет выглядеть так: [-21 ,13, -8, 5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

n = 8

def NegaFib(n):
    if n == -1:
        return 1
    if n == -2:
        return -1
    else:
        return NegaFib(n+2) - NegaFib(n+1)  
    
def Fib(n):
    if n == 1 or n == 2:
        return 1
    if n == 0:
        return 0
    else:
        return Fib(n-1) + Fib(n-2)

list = []
for i in range(-n, 0):
    list.append(NegaFib(i))
for j in range(0, n+1):
    list.append(Fib(j))
print(list)

