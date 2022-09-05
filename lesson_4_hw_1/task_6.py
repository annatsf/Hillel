""" Функція, що приймає безкінечну кількість чисел 
позиційними параметрами та іменований параметр start.
Функція має повертати суму усіх переданих параметрами чисел та числа start

"""


def my_sum(*my_digits, start=0):
    my_array = []
    for i in my_digits[0]:
        my_array.append(int(i))
    return sum(my_array, start)


def main():
    my_digits = input("Enter digits through space: ").split()

    print(my_sum(my_digits))


if __name__ == "__main__":
    main()
