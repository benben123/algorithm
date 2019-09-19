class Solution:
    def searchInsertPst(self, lst, val):
        if lst[0] > val:
            return 0
        if lst[-1] < val:
            return len(lst)
        for i in range(len(lst)):
            if lst[i] == val:
                return i
            if lst[i] < val < lst[i + 1]:
                return i+1
        return len(lst)+1


class Solution2:
    def searchInsertPst2(self, lst, val):
        l, r = 0, len(lst)
        while l < r:
            m = (l + r)/2
            if lst[m] == val:
                return m
            if lst[m] < val:
                l = m + 1
            else:
                r = m
        if lst[m] < val:
            return m + 1
        else:
            return m


if __name__ == '__main__':
    lst = [1,3,5, 6]
    val = 9
    test = Solution()
    testVal = test.searchInsertPst(lst, val)
    print testVal
    test2 = Solution2()
    testVal2 = test2.searchInsertPst2(lst, val)
    print testVal2

