"""
3Sum Closest
Given an array S of n integers, find three integers in S such that
the sum is closest to a given number, target. Return the sum of the three integers.
Example 1:

Input:[2,7,11,15],3
Output:20
Explanation:
2+7+11=20
Example 2:

Input:[-1,2,1,-4],1
Output:2
Explanation:
-1+2+1=2
"""
class Solution:
    def getClosest(self, arry, target):
        sumVal, diff = 0, 0
        length = len(arry)
        if length < 3:
            return None
        if length == 3:
            return sum(arry)
        arry.sort()
        for i in range(length-2):
            l, r = i+1, length - 1
            if i > 0 and arry[i] == arry[i-1]:
                continue
            while l < r:
                temSum = arry[l] + arry[i] + arry[r]
                temDiff = abs(temSum - target)
                if temSum > target:
                    if temDiff < diff:
                        diff = temDiff
                        sumVal = temSum
                    r -= 1
                elif temSum < target:
                    l += 1
        return sumVal

