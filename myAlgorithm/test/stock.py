"""
when would be the best time to sell stock?
"""

class Sol:
    def getLarge(self, nums):
        if len(nums) == 0:
            return 0
        min = nums[0]
        large = 0
        for i in range(1, len(nums)):
            if nums[i] < min:
                min = nums[i]
            else:
                large = max(large, nums[i]-min)
        return large


if __name__ =='__main__':
    nums = [5, 19, 1, 8, 7, 10, 2]
    test = Sol()
    print test.getLarge(nums)
