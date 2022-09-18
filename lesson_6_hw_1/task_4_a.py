"""Написати функцію, що повертає найбільшу цифру випадково 
згенерованого 12-ти-значного натурального числа. 
а) з використанням рядків б) без використання рядків.

"""

from random import randint


def get_max_digit(number): # returns int
    length = 12
    range_start = 10**(length-1)
    range_end = (10**length)-1
    number = randint(range_start, range_end)
    my_list = list(str(number))
    return max(my_list)

def main():
    number = ''
    print(get_max_digit(number))

if __name__ == "__main__":
    main()