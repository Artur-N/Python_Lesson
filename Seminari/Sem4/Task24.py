# В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов.
#  Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list1 = [1.1, 1.2, 3.1, 5, 10.01]
list2 = []

for i in list1:
    if type(i) == float:
        list2.append(round(i - i//1, 2))
    
print(list2)

a = max(list2)
b = min(list2)
print(round(a-b, 2))