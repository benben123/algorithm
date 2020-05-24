"""
Partition array
Given an array nums of integers and an int k, partition the array (i.e move the elements in "nums") such that:

All elements < k are moved to the left
All elements >= k are moved to the right
Return the partitioning index, i.e the first index i nums[i] >= k.

Note: this question is a quick sort question, it is important to know this module
Time: O(n), Space: O(1)
"""

class QuickSort:
    def partitionArray(self, arry, k):
        left, right = 0, len(arry) -1
        while left <= right: #key module
            while left <= right and arry[left] < k:  #key module
                left += 1
            while left <= right and arry[right] >= k: #key module
                right -= 1
            if left <= right: #key module
                arry[left], arry[right] = arry[right], arry[left]
                left += 1
                right -= 1
            return left