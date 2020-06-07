"""
Array [3, 32, 321], find the smallest arranged number, the number should be 321323
"""
class Solution:
    def getSmallest(self, array):
        if len(array) == 0:
            return 0
        def compare(a, b):
            if int(str(a) + str(b)) < int(str(b) + str(a)):
                return -1
            elif int(str(a) + str(b)) > int(str(b) + str(a)):
                return 1
            else:
                return 0
        temp = sorted(array, cmp=compare)
        return int("".join(str(i) for i in temp))

    def getSmallest2(self, array):
        if len(array) == 0:
            return 0
        def compare2(a, b):
            if a + b < b + a:
                return -1
            elif a + b > b + a:
                return 1
            else:
                return 0
        nums = map(str, array)
        temp = sorted(nums, cmp = compare2)
        return "".join(temp)


if __name__ == "__main__":
    array = [3, 32, 321]
    test = Solution()
    val = test.getSmallest(array)
    val2 = test.getSmallest2(array)
    print val
    print val2
