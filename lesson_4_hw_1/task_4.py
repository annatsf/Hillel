"""Програма зчитує ціле число та виводить текст

"""


def integer_digit(d):

    d1 = d + 1
    d2 = d - 1
    return (
        f"Next number for number {d} is {d1} \nPrevious number for number {d} is {d2}"
    )


def main():
    d = int(input("Please enter an integer number: "))
    print(integer_digit(d))


if __name__ == "__main__":
    main()
