""" Function 'Fizz Buzz

"""
def fizz_buzz(first, last):
    result = ''
    while first <= last:
        if result:
            result += '\n'
        if first % 15 == 0:
            result += 'FizzBuzz'
        elif first % 3 == 0:
            result += 'Fizz'
        elif first % 5 == 0:
            result += 'Buzz'
        else:
            result += str(first)
        first += 1
    return result


def main():
    print(fizz_buzz(1, 100))

if __name__ == "__main__":
    main()
