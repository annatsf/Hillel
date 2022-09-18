"""Написати функцію, що знаходить різницю між сумою усіх парних чисел 
та сумою усіх непарних чисел серед num_limit випадкових чисел 
згенерованих в заданому діапазоні lower_bound..upper_bound. 
Для генерації чисел використайте модуль random (можна використати будь-яку зі зручних для вас функцій модулю, наприклад randint)."""

from random import randint
def diff_odd_even(num_limit, lower_bound, upper_bound):
     
    diff = 0
    sum_even = 0
    sum_odd = 0
    for _ in range(num_limit):
        elem = randint(lower_bound, upper_bound)
        if elem % 2 == 0:
           sum_even += elem
        else:
            sum_odd += elem
    diff = sum_even - sum_odd
    return diff

def main():
    num_limit = int(input('Enter limit: '))
    lower_bound = int(input('Enter lower: '))
    upper_bound = int(input('Enter upper: '))
    
    print('Result: ', diff_odd_even(num_limit, lower_bound, upper_bound))



if __name__ == "__main__":
    main()

