class Sol:
    def getMini(self, lst):
        l, r = 0, len(lst)-1
        if r == 0:
            return None
        while l < r:
            mid = (l+r)/2
            if lst[mid] > lst[r]:
                l = mid + 1
            elif lst[mid] < lst[r]:
                r = mid
            else:
                l = l + 1
        return lst[r]


if __name__ == '__main__':
    lst1 = [0, 1, 2, 4, 5, 6, 7]
    lst2 = [4, 5, 6, 7, 0, 1, 2]
    lst3 = [5, 6, 7, 0, 1, 2, 4]
    lst4 = [1, 1, 1, 0, 1]
    test = Sol()
    print test.getMini(lst1)
    print test.getMini(lst2)
    print test.getMini(lst3)
    print test.getMini(lst4)