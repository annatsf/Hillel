"""Площадь и периметр прямоугольного треугольника

"""

from math import sqrt


def triangle_square_and_perimeter(a, b):
    c = sqrt(a**2 + b**2)
    square = round((a * b / 2), 2)
    perimeter = round((a + b + c), 2)
    return square, perimeter


def main():
    a = int(input("Enter the length of the 1st cathetus: "))
    b = int(input("Enter the length of the 2nd cathetus: "))
    e, f = triangle_square_and_perimeter(a, b)
    print("Square is %.2f" % e)
    print("Perimeter is %.2f" % f)


if __name__ == "__main__":
    main()
