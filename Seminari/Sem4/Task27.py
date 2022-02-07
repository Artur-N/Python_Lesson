# Строка содержит набор чисел. Показать большее и меньшее число. Символ-разделитель - пробел.

st1 = '11 2 3 46 5 6 75 8'

def MaxMinStr(s):
    b = []
    for i in s.split():
        b.append(int(i))
    return b               # Вариант записи: return [int(i) for i in s.split()]
print(max(MaxMinStr(st1)), min(MaxMinStr(st1)))

