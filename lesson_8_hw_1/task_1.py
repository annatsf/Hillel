"""Дано довільний список. Створити функцію index(lst, elem), 
що повертатиме індекс elem в списку lst, або, якщо елемент 
відсутній, то None."""


def index(lst, elem):
    if elem in lst:
        index = [i for i in range(0, len(lst)) if lst[i] == elem]
        return index
    else:
        return None


def main():
    my_list = input("Enter list: \n >>>")
    element = input("Enter element from list: \n >>>")
    print(index(my_list, element))


if __name__ == "__main__":
    main()
