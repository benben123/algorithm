# https://www.geeksforgeeks.org/print-all-combinations-of-given-length/

class Solution:
    def printAllKLength(self, set, k):
        n = len(set)
        self.printAllKLengthRec(set, "", n, k)
        # tell what is input and output so that divide different parameters for recursion

    def printAllKLengthRec(self, set, prefix, n, k):
        if k == 0:        # end point
            print prefix
            return
        for i in range(n):
            newprefix = prefix + set[i]
            self.printAllKLengthRec(set, newprefix, n, k-1)


if __name__=="__main__":
    set = ['a', 'b']
    k = 3
    test = Solution().printAllKLength(set, k)
