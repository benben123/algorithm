# coding=utf-8
"""
Given an array consisting of n integers, find the contiguous subarray of given length k
that has the maximum average value. And you need to output the maximum average value.

Example 1:

Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75


Note:

1 <= k <= n <= 30,000.
Elements of the given array will be in the range [-10,000, 10,000].


1. float calculation，cannot use '/' directly, otherwise it will be an integer
2. i+k-1 note, this can avoid overflow
"""

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        length = len(nums)
        if length == k:
            return sum(nums)/float(k)
        maxVal = -10001
        for i in range(length-k+1):
            locVal = sum(nums[i:i+k])
            print locVal
            if maxVal < locVal:
                maxVal = locVal
        return maxVal/float(k)

    def findMaxAverage2(self, nums, k):
        length = len(nums)
        maxVal = sum(nums[:k])
        locVal = maxVal
        for i in range(1, length - k + 1):
            locVal -= nums[i - 1]
            locVal += nums[i + k - 1]
            if maxVal < locVal:
                maxVal = locVal
        return float(maxVal) / k

if __name__== "__main__":
    nums=[1,12,-5,-6,50,3]
    k = 4
    test = Solution().findMaxAverage(nums, k)
    print test