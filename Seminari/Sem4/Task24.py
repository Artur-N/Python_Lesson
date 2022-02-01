# В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов.
#  Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list1 = [1.1, 1.2, 3.1, 5, 10.01]
list2 = []

def Task24(list1):
    for i in list1:
        if type(i) == float:
            list2.append(round(i - i//1, 2))
    # print(list2)
    return round(max(list2) - min(list2), 2)
print(Task24(list1))
