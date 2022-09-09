""" Функція, що приймає безкінечну кількість чисел 
позиційними параметрами та іменований параметр start.
Функція має повертати суму усіх переданих параметрами чисел та числа start

"""


def my_sum(*my_digits, start=0):
    return sum(my_digits[0], start)



def main():
    my_digits = input("Enter digits through space: ").split()
    my_array = []
    for i in my_digits:
         my_array.append(int(i))

    print(my_sum(my_array))


if __name__ == "__main__":
    main()
