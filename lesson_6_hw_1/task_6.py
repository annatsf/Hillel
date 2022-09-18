"""
 Написати функцію, що розраховує суму Unicode кодів усіх символів, 
 що знаходяться між двома заданими символами включно"""
from math import *

def sum_symbol_codes(first, last):
    lst = [i for i in range(first, last + 1)]
    result = sum(lst)
    return result


def main():
    first_symbol = ord(input('Enter first symbol: '))
    last_symbol = ord(input('Enter last symbol: '))
    print(first_symbol, last_symbol)
    print(sum_symbol_codes(first_symbol, last_symbol))

if __name__ == "__main__":
    main()