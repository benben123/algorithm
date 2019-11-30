def myfun(s):
    return s[-1]


def sortList(lst):
    return sorted(lst, key=myfun)


if __name__ == '__main__':
    lst = ['xc', 'zb', 'yd', 'wa']
    print sortList(lst)

