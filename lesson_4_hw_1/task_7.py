""" Функція розраховує суму цифр числа. 
Не можна використовувати будь-яке інше явне чи неявне приведення рядку до числа

"""


def sum(numbers):

    sum = 0
    for i in numbers:
        d = ord(i) - ord("0")
        sum = d + sum

    return f"Sum of digits is {sum}"


numbers = input("Enter a three-digit number: ")


def main():
    print(sum(numbers))


if __name__ == "__main__":
    main()
