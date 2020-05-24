"""
Partition Array by Odd and Even
Partition an integers array into odd number first and even number second.

Example
Example 1:

Input: [1,2,3,4]
Output: [1,3,2,4]
Example 2:

Input: [1,4,2,3,5,6]
Output: [1,3,5,4,2,6]
"""

class Solution:
    """
    @param: nums: an array of integers
    @return: nothing
    """
    def partitionArray(self, nums):
        # write your code here
        left, right = 0, len(nums)-1
        while left <= right:
            while left <= right and nums[left] % 2 == 1:
                left += 1
            while left <= right and nums[right] % 2 == 0:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        return nums
