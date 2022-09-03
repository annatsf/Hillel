from math import cos, pi


def degrees2radians(degrees):
    radiants = (degrees * pi) / 180
    c = round(cos(radiants), 2)
    return c


print(degrees2radians(60))
print(degrees2radians(45))
print(degrees2radians(40))
