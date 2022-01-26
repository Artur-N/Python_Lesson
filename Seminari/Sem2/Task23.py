# 23. Показать таблицу квадратов чисел от 1 до N

n = int(input('N = '))
def SquareTabl(n):
    square = []
    for i in range(n):
        square.append((i+1)**2)
        # print(f'Квадрат {i+1} = {(i+1)**2}')
    return square
print(SquareTabl(n))
