# # Задать список из N элементов, заполненных числами из [-N, N]. 
# # Найти произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

import random 
n = 10
listN = [random.randint(-n, n) for i in range(n)]
print(listN)

def MultiElements(list):
    data = open('file.txt', 'r')
    multi = 1
    for line in data:
        print(f'{int(line)}: {list[int(line)]}')
        multi *= list[int(line)]
    data.close()
    return multi
print(MultiElements(listN))