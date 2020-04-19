"""
Description
中文

English
Given n pieces of wood with length L[i] (integer array). Cut them into small pieces to guarantee you could have equal or more than k pieces with the same length. What is the longest length you can get from the n pieces of wood? Given L & k, return the maximum length of the small pieces.
You couldn't cut wood into float length.
If you couldn't get >= k pieces, return 0.
Have you met this question in a real interview?  Yes
Problem Correction
Example
Example 1

Input:
L = [232, 124, 456]
k = 7
Output: 114
Explanation: We can cut it into 7 pieces if any piece is 114cm long, however we can't cut it into 7 pieces if any piece is 115cm long.
Example 2

Input:
L = [1, 2, 3]
k = 7
Output: 0
Explanation: It is obvious we can't make it.
"""
class WoodCut:
    def woodCut(self, nums, k):
        #此题不是二分法查找数组，而是二分法来计算租内最长值
        start, end = 1, max(nums)
        while start + 1 < end:
            mid = (start + end) /2
            if self.getPieces(nums, mid) >= k:
                start = mid
            else:
                end = mid
        if self.getPieces(nums, start) >= k:
            return start
        if self.getPieces(nums, end) >= k:
            return end
        return 0

    def getPieces(self, nums, L):
        pieces = 0
        for ele in nums:
            pieces += ele/L
        return pieces
