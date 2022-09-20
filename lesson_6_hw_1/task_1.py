""" Function 'Fizz Buzz
"""

def fizz_buzz(first, last):
    result = []
    for i in range(first, last+1):
        if i % 15 == 0:
            result.append('FizzBuzz')
        elif i % 3 == 0:
            result.append('Fizz')
        elif i % 5 == 0:
            result.append('Buzz')
        else:
            result.append(str(i))
    return result
        
def main():
    print('\n'.join(fizz_buzz(1, 100)))

if __name__ == "__main__":
    main()
