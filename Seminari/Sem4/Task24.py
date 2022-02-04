# В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов.
#  Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

lst = [1.1, 1.2, 3.1, 5, 10.01]

def Task24(list):
    list2 = []
    for i in list:
        if type(i) == float:
            list2.append(round(i - i//1, 2))
    # print(list2)
    return round(max(list2) - min(list2), 2)
print(Task24(lst))
