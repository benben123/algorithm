"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        l, r = 0, length - 1
        if length == 0:
            return [-1, -1]
        while l + 1 < r:
            mid = (l + r) / 2
            if nums[mid] < target:
                l = mid
            elif nums[mid] == target:
                res = self.findNeighbour(mid, nums)
                return res
            else:
                r = mid
        if nums[l] == target:
            res = self.findNeighbour(l, nums)
            return res
        if nums[r] == target:
            res = self.findNeighbour(r, nums)
            return res
        return [-1, -1]


    def findNeighbour(self, val, nums):
        length = len(nums)
        l, r = val, val
        while l >= 0 and nums[val] == nums[l]:
            l -= 1
        while r < length and nums[val] == nums[r]:
            r += 1
        return [l + 1, r - 1]
