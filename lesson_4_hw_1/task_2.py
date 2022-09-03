"""площадь и периметр прямоугольного треугольника

"""

from math import sqrt

a = float(input("Enter the length of the 1st cathetus: "))
b = float(input("Enter the length of the 2nd cathetus: "))


def triangle_square_and_perimeter(a, b):
    c = sqrt(a ** 2 + b ** 2)
    # проверка, прямоугольный ли треугольник
    if c ** 2 == a ** 2 + b ** 2:

        s = round((a * b / 2), 2)
        p = round((a + b + c), 2)
        return f"Square: {s} \nPerimeter: {p}"

    else:
        return f"This triangle is not rectangular"


print(triangle_square_and_perimeter(a, b))
