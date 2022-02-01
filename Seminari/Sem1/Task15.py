# 15. Дано число. Проверить кратно ли оно 7 и 23

a = 161
def Check(a):
    return a % 7 == 0 & a % 23 == 0
print(Check(a))
