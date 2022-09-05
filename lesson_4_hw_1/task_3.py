""" Площадь и обьем конуса

"""

from math import pi, sqrt


def cone_square_and_volume(radius, height):

    # площадь основания конуса s1=pi*R^2
    s1 = round((pi * radius**2), 2)
    l = sqrt(radius**2 + height**2)

    # площадь боковой поверхности конуса s2=pi*R*l, где l - образующая
    s2 = pi * radius * l

    square = round((s1 + s2), 2)
    volume = round(((pi * radius**2) * height) / 3)

    return square, volume


def main():
    radius = float(input("Enter the radius: "))
    height = float(input("Enter the height: "))
    s, v = cone_square_and_volume(radius, height)

    print("Square %.2f" % s)
    print("Volume %.2f" % v)


if __name__ == "__main__":
    main()
