import math

r = int(input("Введите радиус: "))
h = int(input("Введите высоту: "))
def radius(r, h):
    side = 2 * math.pi * r * h
    return side
def fullP(side, r):
    s = math.pi * (r ** 2)
    full = side + 2 * s
    return full
side = radius(r, h)
full = fullP(side, r)
print(side)
print(full)

