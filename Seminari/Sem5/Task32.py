# Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

lst = [10, 2, 3, 5, 1, 5, 3, 10, 1, 2 ,3, 5, 10]
lst2 = []
for i in range(len(lst)):
    a = 0
    for j in range(len(lst2)):
        if lst[i] == lst2[j]:
            a += 1
    if a == 0:
        lst2.append(lst[i])
print(lst2)

# 2й вариант
# def get_unic_value(list):
#     return [i for i in set(list)]

# print(get_unic_value(lst))

