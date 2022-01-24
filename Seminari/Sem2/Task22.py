# 22. Найти расстояние между точками в пространстве 2D/3D

def Distance(x1, x2, y1, y2):
    return round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, 2)
print(Distance(1, 4, 1, 5))

def Distance(x1, x2, y1, y2, z1, z2):
    return round(((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5, 2)
print(Distance(1, 2, 1, 3, 1, 4))
