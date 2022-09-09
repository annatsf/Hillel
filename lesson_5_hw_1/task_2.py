"""функція для рішення квадратних рівнянь

"""

from math import sqrt


def solve_quadratic_equation(a, b, c):

    discriminant = b**2 - 4 * a * c

    # If discriminant < 0, then no roots of the quadratic equation
    if discriminant < 0:
        x1 = x2 = None
        return x1, x2

        # If discriminant is 0, then roots of the quadratic equation 1.
    if discriminant == 0:
        x1 = (-b - sqrt(discriminant)) / (2 * a)
        x2 = x1
        return x1, x2

        # If discriminant > 0, then roots of the quadratic equation 2.
    x1 = (-b - sqrt(discriminant)) / (2 * a)
    x2 = (-b + sqrt(discriminant)) / (2 * a)
    return x1, x2


def main():

    print("enter the coefficients of the quadratic equation:")

    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    x1, x2 = solve_quadratic_equation(a, b, c)

    if x1 == x2 and x1 is not None:
        print(f"x = {x1}")

    elif x1 is not None and x2 is not None:
        print("x1 = %.2f \nx2 = %.2f" % (x1, x2))

    else:
        print("Корней нет")


if __name__ == "__main__":
    main()
