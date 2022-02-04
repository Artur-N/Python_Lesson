# Найти сумму чисел списка стоящих на нечетной позиции

lst = [9, 8, 7, 6, 5, 4, 3, 2, 1]

def SumOddIndex(list):
    return sum(list[1::2])
    # sum = 0
    # for i in range(1, len(list), 2):
    #     sum += list[i]
    # return sum
print(SumOddIndex(lst))