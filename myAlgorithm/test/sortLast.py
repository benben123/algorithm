def sortLast(a):
    return a[-1]


def sort_last(any):
    return sorted(any, key=sortLast)


if __name__ == "__main__":
    tuple1 = [(2, 9), (1, 3), (3, 4, 5), (1, 7)]
    string1 = ['dbc', "abf", "acd"]
    print sort_last(tuple1)
    print sort_last(string1)

