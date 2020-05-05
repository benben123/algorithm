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

"""

"""
1. float 的计算，不能直接用 "/" 否则得到的是一个整数
2. i+k-1 的标注，这样防止超过界限
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
            """
            :type nums: List[int]
            :type k: int
            :rtype: float
            """
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
    test = Solution().findMaxAverage2(nums, k)
    print test