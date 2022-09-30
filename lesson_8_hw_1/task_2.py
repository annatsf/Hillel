"""Створити функцію copydeep(lst), що створює глибоку копію довільного списку

"""


def copydeep(lst):
    if not isinstance(lst, list):
        return lst
    else:
        copy_lst = []
        for next_lst in lst:
            copy_lst.append(copydeep(next_lst))
        return copy_lst


def main():
    lst1 = ["a", 1, 2.0, ["b"]]
    lst2 = copydeep(lst1)
    lst1[3].append(0)
    # print(lst1[3], lst2[3])
    print(lst2)


if __name__ == "__main__":
    main()
