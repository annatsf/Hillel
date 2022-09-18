"""Написати функцію, що повертає найбільшу цифру випадково 
згенерованого 12-ти-значного натурального числа. 
а) з використанням рядків б) без використання рядків.

"""

from random import randint


def get_max_digit(number):


    max_dig = number % 10
    number = number // 10
    while number > 0:
        
        if max_dig < number %10:
            max_dig = number %10
        number = number // 10
    return max_dig



def main():
    length = 12
    range_start = 10**(length-1)
    range_end = (10**length)-1
    number = randint(range_start, range_end)
    print(number)

    print(get_max_digit(number))

if __name__ == "__main__":
    main()