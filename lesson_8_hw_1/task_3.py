"""Дано список з чисел та рядків. Рядки у списку завжди 
непорожні та складаються тільки з символів 0123456789. 
За допомогою функції sorted() отримати копію цього списку:

a) відсортовану за значенням числа елементу
б) відсортовано за значенням першої цифри числа. 
"""


def my_key_a(element):
    return float(element)


def my_key_b(element):
    return str(element)[0]


def main():
    my_list_a = [5, "9", 0, "452", 6.5, "6", 1, 2]
    my_list_b = [472, 326, 1, "1101000", 9, "20", 863, "0"]
    print(sorted(my_list_a, key=my_key_a))
    print(sorted(my_list_b, key=my_key_b))


if __name__ == "__main__":
    main()
