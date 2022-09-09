"""Потрібно визначити, чи є рік із цим числом високосним

"""


def is_year_leap(year):
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        return "YES"
    else:
        return "NO"


def main():

    year = int(input("Enter year: "))

    print(is_year_leap(year))


if __name__ == "__main__":
    main()
