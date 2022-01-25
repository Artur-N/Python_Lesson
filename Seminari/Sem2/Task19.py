# 19. Определить номер четверти плоскости, в которой находится точка с координатами Х и У, причем X ≠ 0 и Y ≠ 0

x = int(input('x = '))
y = int(input('y = '))

def Quarter(x, y):
    if x > 0 < y:
        return 1
    elif x < 0 < y:
        return 2
    elif x < 0 > y:
        return 3
    elif x > 0 > y:
        return 4
print(f'Точка с координатами x = {x} и y = {y} находиться в {Quarter(x, y)}й четверти')


