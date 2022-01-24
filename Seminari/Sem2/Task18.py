# 18. Проверить истинность утверждения ¬(X ⋁ Y) = ¬X ⋀ ¬Y

x = [0, 1]
y = [0, 1]

def TruthChec(x, y):
    for x in range(2):
        for y in range(2):
            res = not(x or y) == (not x and not y)
            print(x, y, res)
TruthChec(x, y)