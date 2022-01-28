# Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.

listDays = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
dayWeek = int(input('Введите день недели: '))

def NumberDayWeek(a, list):
    if 5 < a < 8:
        return f'{list[a-1]} - выходной'
    elif 0 < a < 6:
        return f'{list[a-1]} - рабочий день'
    else:
        return 'Такого дня недели не существует'
print(NumberDayWeek(dayWeek, listDays))

