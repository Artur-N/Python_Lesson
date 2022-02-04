# Найти произведение пар чисел в списке. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 

lst = [2, 3, 4, 5, 6]

def MultiPair(list):
    return [list[i] * list[-i - 1] for i in range(int(len(list) / 2 + 0.5))]
    # b = []
    # for i in range(int(len(list) / 2 + 0.5)):
    #     b.append(list[i] * list[(-i-1)])
    # return b
print(MultiPair(lst)) 

