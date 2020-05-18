"""
Two Sum - Unique pairs
Description

English
Given an array of integers, find how many unique pairs in the array such that their sum is equal to a specific target number. Please return the number of pairs.
Have you met this question in a real interview?  Yes
Problem Correction
Example
Example 1:

Input: nums = [1,1,2,45,46,46], target = 47
Output: 2
Explanation:

1 + 46 = 47
2 + 45 = 47

Example 2:

Input: nums = [1,1], target = 2
Output: 1
Explanation:
1 + 1 = 2
"""
class UniqPair:
    def uniqPair(self, lst, tar):
        lst.sort()
        left, right = 0, len(lst) - 1
        count = 0
        while left < right:
            if lst[left] + lst[right] >tar:
                right -= 1
            elif lst[left] + lst[right] <tar:
                left += 1
            else:
                count += 1
                left += 1
                right -= 1
                while left < right and lst[left] == lst[left-1]:
                    left += 1
                while left < right and lst[right] == lst[right + 1]:
                    right -= 1
        return count
