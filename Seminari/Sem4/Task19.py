# Реализовать алгоритм задания случайных чисел. Без использования встроенного генератора псевдослучайных чисел

import datetime
print(datetime.datetime.now().microsecond)

def Rnd():
# 
    return datetime.datetime.now().microsecond % 100
print(Rnd()) # случайное чисто от 0 до 99


