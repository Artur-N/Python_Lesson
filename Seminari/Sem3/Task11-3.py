# Для натурального N создать список: 1, -3, 9, -27, 81 и т.д.

n = 7

def ListMulti3(n):
    list = []
    for i in range(n):
        if i % 2 == 0:
            list.append(3**i)
        else:
            list.append(-3**i)
    return list
print(ListMulti3(n))
