"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
"""

class RotatedArray(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        start = length - k
        part = []
        for i in range(k):
            part.append(nums.pop())
        part = part[::-1]
        part.extend(nums)
        return part


    def rotate2(self, nums, k):
        length = len(nums)
        start = length - k
        res = []
        for i in range(start, length):
            res.append(nums[i])
        for j in range(0, start):
            res.append(nums[j])
        return res

    def rotate3(self, nums, k):
        length = len(nums)
        if length == 0 or length == 1:
            return nums
        l, r = 0, length - 1
        k = k % length
        if k:
            self.swap(nums, l, r)
            l, r = 0, k - 1
            self.swap(nums, l, r)
            l, r = k, length - 1
            self.swap(nums, l, r)
        return nums

    def swap(self, nums, l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        return nums

    def rotate4(self, nums, k):
        n = len(nums) - k
        nums[:] = nums[n:] + nums[:n]
        return nums

if __name__ == "__main__":
    nums= [1,2,3,4,5,6,7]
    k =3
    test = RotatedArray().rotate(nums,k)
    print "test1 result:"
    print test
    nums2= [1,2,3,4,5,6,7]
    test2 = RotatedArray().rotate2(nums2, k)
    print "test2 result"
    print test2
    nums3= [1,2,3,4,5,6,7]
    test3 = RotatedArray().rotate3(nums3, k)
    print "test3 result"
    print test3