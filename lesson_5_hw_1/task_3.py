"""функція, що відповідає на питання, чи перетинають два заданих кола на площині. Кожне коло задається координатами центра та радіусом

"""

from math import sqrt


def circles_intersect(x1, y1, r1, x2, y2, r2):

    # two circles intersect if the distance between their centres is less than the sum of their radiuses
    d = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    if d < r1 + r2:
        return True
    else:
        return False


def main():
    print("Enter the coordinates of the circle centres and their radiuses ")
    x1 = int(input("x1 = "))
    y1 = int(input("y1 = "))
    r1 = int(input("r1 = "))
    x2 = int(input("x2 = "))
    y2 = int(input("y2 = "))
    r2 = int(input("r2 = "))
    if circles_intersect(x1, y1, r1, x2, y2, r2) is True:
        print("The circles intersect")
    else:
        print("The circles do not intersect")


if __name__ == "__main__":
    main()
