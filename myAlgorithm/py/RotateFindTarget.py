"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        length = len(nums)
        l, r = 0, length-1
        while l+1 < r:
            mid = (l+r)/2
            if nums[mid] >= nums[l]:
                if nums[l] <= target <= nums[mid]:  # 找到可以进行比较的一边，同时注意等号的添加
                    r = mid
                else:
                    l = mid
            else:
                if nums[mid] <= target <= nums[r]:  # 找到可以进行比较的一边
                    l = mid
                else:
                    r = mid
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        return -1