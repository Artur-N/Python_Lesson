# 0. Вывести квадрат числа

number = int(input('Введите число: '))
print(f'Квадрат {number} равен {number**2}')

def Square(a):
    return a**2

print(f'Квадрат {number} равен {Square(number)}')
