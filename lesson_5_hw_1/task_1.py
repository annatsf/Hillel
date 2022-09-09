"""Функція, що визначає чи введене число є парним

"""


def is_even(number):
    # четное число должно делиться без остатка на 2
    return number % 2 == 0


def main():
    number = int(input("Enter number: "))
    print(is_even(number))


if __name__ == "__main__":
    main()
