"""функція sign() та для введеного користувачем числа x виведіть значення sign(x)

"""


def sign_of_digit(x):
    """
    sign(x) = 1, якщо x > 0,
    sign(x) = -1, якщо x < 0,
    sign(x) = 0 якщо x = 0.

    """
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


def main():
    x = int(input("Enter a value of x: "))
    print("sign(x) = ", sign_of_digit(x))


if __name__ == "__main__":
    main()
