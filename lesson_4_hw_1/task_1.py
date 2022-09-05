""" Функція переводить градуси в радіани.
Використовуючи цю функцію, вивести на екран значення 
косинусів кутів 60, 45 та 40 градусів

"""

from math import cos, pi


def degrees2radians(degrees):

    # используем формулу перевода градусов в радианы
    radiants = (degrees * pi) / 180

    return radiants


def main():
    print(round(cos(degrees2radians(60)), 2))
    print(round(cos(degrees2radians(45)), 2))
    print(round(cos(degrees2radians(40)), 2))


if __name__ == "__main__":
    main()
