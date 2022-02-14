# Составить список простых множителей натурального числа N

n = int(input('N = '))
div = 2
list = []
while n > 1:
    while n % div == 0:
        list.append(div)
        n /= div
    div += 1
print(f'Список простых множителей: {list}')