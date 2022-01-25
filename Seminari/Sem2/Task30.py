# 30. Показать кубы чисел, заканчивающихся на четную цифру

def EvenCube(a):
    for i in range(a):
        if i**3 % 2 == 0:
            print(i**3, end=' ')
EvenCube(10)

