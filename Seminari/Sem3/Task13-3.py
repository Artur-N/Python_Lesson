# 13. Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

str1 = 'qwer tyqwerty trert'  # input('1я строка: ')
str2 = 'tyq'  # input('2я строка: ')

def Strings2(s1, s2):
    s = 0
    while s2 in s1:
        s += 1
        s1 = s1[s1.find(s2)+len(s2):]
    return s
print(Strings2(str1, str2))

# 2й способ

print(str1.count(str2))
