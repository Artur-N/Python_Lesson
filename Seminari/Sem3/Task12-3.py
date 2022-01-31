# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3k + 1.

n = 5

def Task12(a):
    diction = {}
    for k in range(1, n + 1):
        diction[k] = 3 * k + 1
    return diction

print(Task12(n))
