# 18. Проверить истинность утверждения ¬(X ⋁ Y) = ¬X ⋀ ¬Y

def TruthChec(x, y):
    return not(x or y) == (not x and not y)

for x in range(2):
    for y in range(2):
        print(x, y, TruthChec(x, y))

