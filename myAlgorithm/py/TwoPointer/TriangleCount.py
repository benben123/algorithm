"""
Triangle Count
Given an array of integers, how many three numbers can be found in the array, so that we can build an
triangle whose three edges length is the three numbers that we find?
Example
Example 1:

Input: [3, 4, 6, 7]
Output: 3
Explanation:
They are (3, 4, 6),
         (3, 6, 7),
         (4, 6, 7)
Example 2:

Input: [4, 4, 4, 4]
Output: 4
Explanation:
Any three numbers can form a triangle.
So the answer is C(3, 4) = 4
"""

class Solution:
    def getNumbers(self, lst):
        count = 0
        lst.sort()
        for i in range(len(lst)):
            l, r = 0, i-1
            """
            note: r value here, r takes one position before the largest one, this is a good way
            to track all the three numbers
            """
            while l < r:
                if lst[l] + lst[r] > lst[i]:
                    count += r - l
                    r -= 1
                else:
                    l += 1
        return count