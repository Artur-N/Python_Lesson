# 13. Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

s1 = 'qwer tyqwerty trert' # input('1я строка: ')
s2 = 'qw' # input('2я строка: ')
def Strings2(s1, s2):
    s = 0
    for i in range(len(s1)):
        if s2 in s1:
            s += 1
            s1 = s1[i:len(s1)]
    return s
print(Strings2(s1, s2))

# print(s1.count(s2))