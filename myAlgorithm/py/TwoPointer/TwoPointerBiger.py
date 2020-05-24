"""
numbers = [2, 7, 11, 15], target = 24
how many pairs sum are bigger than target?
"""

class Solution:
    def countPairs(self, lst, target):
        l, r = 0, len(lst) - 1
        count = 0
        lst.sort()
        while l < r:
            if lst[l] + lst[r] > target:
                count += r - l
                r -= 1
            else:
                l += 1
        return count