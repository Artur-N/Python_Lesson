# Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

lst = [10, 10, 2, 2, 3, 5, 1, 5, 3, 10, 1, 2 ,3]
print(lst)
def Uniq_Seq(list):
    list2 = []
    for i in range(len(list)):
        a = 0
        for j in range(len(list2)):
            if list[i] == list2[j]:
                a += 1
        if a == 0:
            list2.append(list[i])
    return list2
print(Uniq_Seq(lst))

# 2й вариант
# def get_unic_value(list):
#     return [i for i in set(list)]

# print(get_unic_value(lst))

