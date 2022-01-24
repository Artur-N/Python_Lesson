# 20. Задать номер четверти, показать диапазоны для возможных координат

a = int(input('Введите номер четверти: '))

def NumberQuarter(a):
    if a == 1:
        print ('x < 0; y > 0')
    elif a == 2:
        print ('x > 0; y > 0')
    elif a == 3:
        print ('x > 0; y < 0')
    elif a == 4:
        print ('x < 0; y < 0')
NumberQuarter(a)    

