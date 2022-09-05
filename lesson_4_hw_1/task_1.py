""" Функція переводить градуси в радіани.
Використовуючи цю функцію, вивести на екран значення 
косинусів кутів 60, 45 та 40 градусів

"""

from math import cos, pi


def degrees2radians(degrees):

    # используем формулу перевода градусов в радианы
    radiants = (degrees * pi) / 180
    # находим косинус
    c = round(cos(radiants), 2)
    return c


def main():
    print(degrees2radians(60))
    print(degrees2radians(45))
    print(degrees2radians(40))


if __name__ == "__main__":
    main()
