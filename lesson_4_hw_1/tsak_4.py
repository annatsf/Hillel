d = int(input("Please enter an integer number: "))


def integer_digit():
    d1 = d + 1
    d2 = d - 1
    return (
        f"Next number for number {d} is {d1} \nPrevious number for number {d} is {d2}"
    )


print(integer_digit())
