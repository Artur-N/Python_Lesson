# 22. Найти расстояние между точками в пространстве 2D/3D

x1 = 1
x2 = 4
y1 = 1
y2 = 5
z1 = 1
z2 = 3

def Distance(x1, x2, y1, y2):
    return round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, 2)
print(Distance(x1, x2, y1, y2))

def Distance(x1, x2, y1, y2, z1, z2):
    return round(((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5, 2)
print(Distance(x1, x2, y1, y2, z1, z2))
