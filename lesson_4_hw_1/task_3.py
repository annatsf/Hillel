""" Площадь и обьем конуса

"""

from math import pi, sqrt


def cone_square_and_volume(radius, height):

    # площадь основания конуса s1=pi*R^2
    s1 = round((pi * radius**2), 2)
    l = sqrt(radius**2 + height**2)

    # проверка треугольника, где катеты - радиус основания и высота
    if l**2 == radius**2 + height**2:

        # площадь боковой поверхности конуса s2=pi*R*l, где l - образующая
        s2 = pi * radius * sqrt(radius**2 + height**2)
    else:
        return f"This Cone does not exist"

    s = round((s1 + s2), 2)
    v = round(((pi * radius**2) * height) / 3)

    return f"Cone Square is: {s} \nCone volume is: {v}"


def main():
    radius = float(input("Enter the radius: "))
    height = float(input("Enter the height: "))
    print(cone_square_and_volume(radius, height))


if __name__ == "__main__":
    main()
