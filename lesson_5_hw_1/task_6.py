"""Рекурсивна функція, що приймає натуральне число і повертає число з послідовності 
Фібоначі, позиція якого відповідає введеному числу

"""


def fibonacci(index):
    if index == 1:
        return 0
    if index == 2:
        return 1

    return fibonacci(index - 1) + fibonacci(index - 2)


def main():

    index = int(input("Enter a number: "))

    print("The number in the Fibonacci sequence is", fibonacci(index))


if __name__ == "__main__":
    main()
