""" Функція, що приймає безкінечну кількість чисел 
позиційними параметрами та іменований параметр start.
Функція має повертати суму усіх переданих параметрами чисел та числа start

"""

def my_sum(my_digits, start=0):
    result = start + sum([int(i) for i in my_digits.split()])
    
    return result
    
    
def main():
    my_digits = input('Enter digits through space: ')
    print(my_sum(my_digits))
    

if __name__ == "__main__":
    main()