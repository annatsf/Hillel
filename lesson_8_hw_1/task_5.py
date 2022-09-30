"""Написати функцію, що повертає усі прості числа від 1 до 100 у вигляді списку.
"""


def gen_primes():
    lst = [2]
    num = 100
    for i in range(3, num + 1, 2):
        k = 0
        for j in lst:
            if i % j == 0:
                k = 1
                break
        if k == 0:
            lst.append(i)
    return lst


def main():

    print(gen_primes())


if __name__ == "__main__":
    main()
