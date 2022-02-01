# 3. По заданному номеру дня недели вывести его название

listDays = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
dayWeek = int(input('Введите день недели: '))
if 0 < dayWeek < 8:
    print(f'{dayWeek}й день недели - {listDays[dayWeek-1]}')
else:
    print('Такого дня недели не существует')

# Функция
def NumberDayWeek(a, list):
    if 0 < a < 8:
        return list[a-1]
    else:
        return 'Такого дня недели не существует'
print(NumberDayWeek(dayWeek, listDays))

