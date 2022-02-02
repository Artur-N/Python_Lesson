# Определить, присутствует ли в заданном списке строк, некоторое число 

lst = ['krm', 'c04', '95', 'h', '03n', '0r', 'm5', 'clekf']
a = 5

def NumberInString(list, a):
    count = 0
    for i in list:
        if str(a) in i:
            count += 1
    if count > 0:
        return True
    else: return False    
print(NumberInString(lst, a))


