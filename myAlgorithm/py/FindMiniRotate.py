class FindMiniRotate:
    def findMiniRotate(self, nums):
        if not nums:
            return -1
        l, r = 0, len(nums) -1
        while l+1 < r:
            mid = (l+r) / 2
            if nums[mid] > nums[r]:
                l = mid
            else:
                r = mid
        return min(nums[l], nums[r])


if __name__ == "__main__":
    nums = [4, 5,6,7,0,1,2]
    test = FindMiniRotate().findMiniRotate(nums)
    print test