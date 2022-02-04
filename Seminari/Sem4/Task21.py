# # # Определить, позицию второго вхождения строки в списке либо сообщить, что его нет.

a = ['ve', 'vqeq', 'vref', 've', 'vke']
b = 've'

k = 0
for i in range(len(a)):
    if b in a[i]:
        k += 1
        if k == 2:
            index = i
if k > 1:
    print(index)
else:
    print('Второго вхождения нет!')


