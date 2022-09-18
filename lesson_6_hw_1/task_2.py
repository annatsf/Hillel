""" Написати функцію, що знаходить різницю між максимальним та мінімальним
значенням з num_limit випадкових чисел згенерованих в заданому діапазоні 
lower_bound..upper_bound.

"""
from random import randint

def diff_min_max(num_limit, lower_bound, upper_bound): 
    diff = 0
    minimal = None
    maximal = None  
    for _ in range(num_limit):
        elem = randint(lower_bound, upper_bound)
        if minimal is None or elem < minimal:
            minimal = elem
        if maximal is None or elem > maximal:
            maximal = elem
    diff = maximal - minimal
    return diff

def main():
    num_limit = int(input('Enter limit: '))
    lower_bound = int(input('Enter lower: '))
    upper_bound = int(input('Enter upper: '))
    
    print('Result: ', diff_min_max(num_limit, lower_bound, upper_bound))



if __name__ == "__main__":
    main()

