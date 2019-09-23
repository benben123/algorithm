class Sol:
    def maxSubArr(self, lst):
        maxT = float('-inf')
        sumT = 0
        start, end = 0, 0
        for i in range(len(lst)):
            for j in range(i, len(lst)):
                sumT += lst[j]
                if sumT >= maxT:
                    maxT = sumT
                    start, end = i, j
            sumT = 0
        return lst[start: end+1], maxT

    def findMaxSubArray(self, nums):
        if max(nums) < 0:
            return max(nums)
        global_max, local_max = float("-inf"), 0
        for x in nums:
            local_max = max(0, local_max + x)
            global_max = max(global_max, local_max)
        return global_max


    def getSubMax(self, nums):
        endingHere = nums[0]
        maxSoFar = nums[0]
        for i in range(1, len(nums)):
            endingHere = max(endingHere + nums[i], nums[i])
            maxSoFar = max(endingHere, maxSoFar)
        return maxSoFar


    def getMaxProduct(self, nums):
        if len(nums) == 0:
            return 0
        minV, maxL, maxG = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            mn = minV
            mx = maxL
            maxL = max(nums[i], nums[i]*mx, nums[i]*mn)
            minV = min(nums[i], nums[i]*mx, nums[i]*mn)
            maxG = max(maxG, maxL)
        return maxG


    def getMaxProduct2(self, nums):
        if len(nums) == 0:
            return 0
        minV, maxL, maxG = 1, 1, float('-inf')
        for ele in nums:
            minV, maxL = min(ele, ele*minV, ele*maxL), max(ele, ele*minV, ele*maxL)
            maxG = max(maxG, maxL)
        return maxG

if __name__ == '__main__':
    lst = [2, 1, -3, 4, -1, 2, 1, -5, 4]
    nums = [2, 3, -2, 4]
    test = Sol()
    # print test.maxSubArr(lst)
    # print test.findMaxSubArray(lst)
    # print test.getSubMax(lst)
    print test.getMaxProduct(nums)
    print test.getMaxProduct2(nums)


