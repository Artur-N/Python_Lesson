# Реализовать алгоритм перемешивания списка.

n = 3
listN = [i for i in range(-n, n+1)]
print(listN)

import random
def Mix(list):
    for i in range(len(list)):
        a = random.randint(i, len(list)-1)
        temp = list[i]
        list[i] = list[a]
        list[a] = temp
    return list
print(Mix(listN))    

        
# 2й способ

random.shuffle(listN)
print (listN)