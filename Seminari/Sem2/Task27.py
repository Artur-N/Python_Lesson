# 27. Определить количество цифр в числе

# 1й способ

a = -97652
if a < 0: a = -a
print(len(str(a)))

# 2й способ

count = 0
while a != 0:
    a = a // 10
    count += 1
print(count)