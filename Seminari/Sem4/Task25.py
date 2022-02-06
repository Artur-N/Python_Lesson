# Написать программу преобразования десятичного числа в двоичное

a = 99

def DecInBin(n):
    bin_n = ''
    while n != 0:
        bin_n += str(n%2)
        n //= 2
    return bin_n[::-1]
print(DecInBin(a))

