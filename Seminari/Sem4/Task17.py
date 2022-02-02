# # Задать список из N элементов, заполненных числами из [-N, N]. 
# # Найти произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

n = 3
listN = [i for i in range(-n, n+1)]
print(listN)

def MultiElements(list):
    data = open('file.txt', 'r')
    multi = 1
    for line in data:
        print(f'{int(line)}: {list[int(line)]}')
        multi *= list[int(line)]
    return multi
print(MultiElements(listN))