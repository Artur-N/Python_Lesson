# 9. Показать последнюю цифру трёхзначного числа

a = -258
if 100 <= a <= 999:
    print(a % 10)
elif -999 <= a <= -100:
    print(-a % 10)
else:
    print('Число не трёхзначное!')

# Функция

def LastNumber(a):
    if 100 <= a <= 999:
        return a % 10
    elif -999 <= a <= -100:
        return -a % 10
    else:
        return 'Число не трёхзначное!'
print(LastNumber(a))