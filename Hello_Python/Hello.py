# Типы данных и переменные
# int, float, boolean, str, list, None

a = 123
b = 1.23

print(type(a))  # показать тип перменной
print(b)

s = 'Hello, World!'  # s = 'Hello, \nWorld!' - с переходом на новую строку
print(s)

print(a, b, s)                            # 123 1.23 Hello, World!
print(a, '-', b, '-', s)                  # 123 - 1.23 - Hello, World!
print('{} - {} - {}'.format(a, b, s))     # 123 - 1.23 - Hello, World!
print('{2} - {0} - {1}'.format(a, b, s))  # Hello, World! - 123 - 1.23
print(f'{s} - {b} - {a}')                 # Hello, World! - 1.23 - 123

f = True  # правда
k = False  # лож
print(f, k)

list = [1, 2, 3]
print(list)
col = ['q', 'w', 'e']
print(col)

# Ввод и вывод данных
# input, print

print('Введите а:')
a = int(input())
print('Введите b:')
b = int(input())
print(a, '+', b, '=', a+b)
print(f'{a} + {b} = {a+b}')

# Арифметические операции
# +, -, *, /, %, **, //

a = 5
b = 2
c = a / b
d = a // b # деление без остатка
g = a % b # остаток от деления
h = a ** b # возведение "a" в степень "b"
print(c)
print(d)
print(g)
print(h)

x = 2.4723418
y = 3
z = round(x * y, 3) # 3 - количество знаков после ,
print(z)

a += 3   # a = a + 3
b *= 3   # b = b * 3
print(a)
print(b)

# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or – не путать с &, |, ^
# Кое-что ещё: is, is not, in, not in

a = 2 < 5 < 8 
print(a)   # True

b = 'qwe'
c = 'qwe'
print(b==c)  # True

d = [1, 2, 3]
f = [1, 2, 3]
print(d != f)  # False
print(3 in d)  # True
print(not 3 in d)  # False

# Управляющие конструкции: if, if-else

a = int(input('a = '))
b = int(input('b = '))
if a > b:
    print(a)
else:
    print(b)

username = input('Введите имя: ')
if username == 'Маша':
    print('Ура! Это же Маша!')
elif username == 'Петя':
    print('Эх, опять Петя.')
else:
    print('Привет,', username)

# Управляющие конструкции: while

original = 123
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
else:
    print('Хватит')
print(inverted)

# Управляющие конструкции: for

list = [1, 2, 3, 4, 5]
for i in list:
    print(i**3)   # Возведение в куб каждое значение из списка list

r = range(100, 0, -20)    # от 100 до 0 с шагом 20
for i in r:
    print(i)          # 100 80 60 40 20

for i in range(5):   # от 0 до 4
    print(i)         # 0 1 2 3 4

for i in 'qwerty':
    print(i)         # q w e r t

# Работа со строками

text = 'съешь ещё этих мягких французских булок'
print(len(text))      			# 39 - количество символов в строке
print('ещё' in text)  			# True
print(text.isdigit()) 			# False, являются ли числами?
print(text.islower()) 			# True, все ли символы маленького регистра
print(text.replace('ещё','ЕЩЁ')) 	# Замена

print(text[0])        # c
print(text[1])        # ъ
print(text[len(text)-1])  # к, последняя буква
print(text[-5])       # б, 5я с конца
print(text[:])        # print(text)
print(text[:2])       # съ, от 1 до 2 буквы, по индексу от 0 до 1
print(text[len(text)-3:])  # лок, от 3й с конца до последней буквы 
print(text[2:9])      # ешь ещё, от 3й до 9й
print(text[6:-18])    # ещё этих мягких
print(text[0:len(text):6])  # сеикакл, от 0 (по индексу) буквы до конца текста с шагом в 6 букв
print(text[::6])      # сеикакл, от начала до конца с шагом 6
text = text[2:9] + text[-5] + text[:2] # ешь ещёбсъ
print(text)

# Работа со списками

numbers = [1, 2, 3, 4, 5]
print(numbers)  # [1, 2, 3, 4, 5]
numbers = list(range(1, 6))
print(numbers)  # [1, 2, 3, 4, 5]
numbers[0] = 10
print(numbers)  # [10, 2, 3, 4, 5]
for i in numbers:
    i *= 2
    print(i)    # [20, 4, 6, 8, 10]
print(numbers)  # [10, 2, 3, 4, 5]

colors = ['red', 'green', 'blue']
for e in colors:
    print(e)  	# red green blue
for e in colors:
    print(e*2)  	# redred greengreen blueblue
colors.append('gray') # добавить в конец
print(colors == ['red', 'green', 'blue', 'gray']) # True
colors.remove('red') # удалить элемент
del colors[0]  # удалить элемент

list = [1, 2, 3, 4, 5]
list.pop() # удаляет последний элемент из списка
print(list) # [1, 2, 3, 4]
list.pop(2) # удаляет 2й элемент из списка
print(list) # [1, 2, 4]
list.insert(2, 10) # вставляет на позицию 2 новый элемент 10
print(list) # [1, 2, 10, 4]
list.append(11) # добавляет значение (11) в конец
print(list) # [1, 2, 10, 4, 11]


# Функции

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return
print(f(1))         # Целое
print(f(2.3))       # 23
print(f(28))        # None

def new_string(symbol, count = 3):
 return symbol * count
print(new_string('!', 5)) # !!!!!
print(new_string('!')) # !!!
print(new_string(4)) # 12

def concatenatio(*params): # (*) передача лубого количества аргументов
 res: str = "" # в даннном случае строки, можно и числа - "res = 0"
 for item in params:
  res += item
 return res
print(concatenatio('a', 's', 'd', 'w')) # asdw
print(concatenatio('a', '1', 'd', '2')) # a1d2
# print(conatenatio(1, 2, 3, 4)) # TypeError: ...

# Файлы
# a – открытие для добавления данных
# r – открытие для чтения данных
# w – открытие для перезаписи данных
# w+, r+

colors = ['red', 'green', 'blue']
data = open('file.txt', 'w') # data - переменная для работы с файлом, open - функция для работы с файлом, # file.txt - текстовый файл.
data.writelines(colors) # разделителей не будет. 
data.write('Line 2\n')
data.close()

# 2й способ записи в файл
with open('file.txt', 'a') as data:
 data.write('line 1\n')
 data.write('line 2\n')

# Чтение из файла
path = 'file.txt'
data = open(path, 'r')
for line in data:
 print(line)
data.close()

# Кортежи. Кортеж – это неизменяемый “список”

t = ()
print(type(t)) # tuple

t = tuple(['red', 'green', 'blue'])
print(t[0]) # red
for e in t:
 print(e) # red green blue

# Словари - Неупорядоченные коллекции произвольных объектов с доступом по ключу

dictionary = {}
dictionary = \
 {
 'up': '↑',
 'left': '←',
 'down': '↓',
 'right': '→'
 }  # \ - перенос на новую строку
print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary['left']) # ←

dictionary['left'] = '⇐' # присвоение ключу 'left' нового значения
print(dictionary['left']) # ⇐

del dictionary['left'] # удаление элемента
for item in dictionary: # for (k,v) in dictionary.items():
 print('{}: {}'.format(item, dictionary[item]))
# up: ↑
# down: ↓
# right: →

for k in dictionary.keys():  # покажет ключи
    print(k) 

for k in dictionary.values():  # покажет значения
    print(k) 

# Множества - Неупорядоченная совокупность элементов

a = {1, 2, 3, 5, 8}
b = {'2', '5', 8, 13, 21}
print(type(b)) # set

a = {1, 1, 1, 1, 1}
print(a) # {1}

colors = {'red', 'green', 'blue'}
print(colors) # {'red', 'green', 'blue'}
colors.add('gray')
print(colors) # {'red', 'green', 'blue','gray'}
colors.remove('red')
print(colors) # {'green', 'blue','gray'}
colors.discard('red') # ok
print(colors) # {'green', 'blue','gray'}
colors.clear() # { }
print(colors) # set()

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy() # c = {1, 2, 3, 5, 8}
u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21} - объединение
i = a.intersection(b) # i = {8, 2, 5} - пересечение
dl = a.difference(b) # dl = {1, 3} 
dr = b.difference(a) # dr = {13, 21}

a = {1, 2, 3, 5, 8}
b = frozenset(a) # Неизменяемое множество
print(b) # frozenset({1, 2, 3, 5, 8})


