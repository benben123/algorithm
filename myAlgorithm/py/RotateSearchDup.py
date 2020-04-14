"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        l, r = 0, len(nums)-1
        while l+1< r:
            mid = l + (r-l)/2
            while l < mid and nums[l] == nums[mid]: # tricky part
                l += 1
            # the first half is ordered
            if nums[l] <= nums[mid]:
                # target is in the first half
                if nums[l] <= target <= nums[mid]:
                    r = mid
                else:
                    l = mid
            # the second half is ordered
            else:
            # target is in the second half
                if nums[mid] <= target <= nums[r]:
                    l = mid
                else:
                    r = mid
        if nums[l] == target:
            return True
        if nums[r] == target:
            return True
        return False