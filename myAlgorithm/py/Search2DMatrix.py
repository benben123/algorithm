"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        length = len(matrix)
        if not matrix or len(matrix[0]) == 0:
            return False
        if length == 1:
            return self.getValue(matrix[0], target)

        row = 0
        l, r = 0, length - 1
        while l + 1 < r:
            mid = (l + r) / 2
            if matrix[mid][0] <= target:
                l = mid
            else:
                r = mid
        if matrix[l][0] <= target < matrix[r][0]:
            row = l
        if matrix[r][0] <= target:
            row = r
        return self.getValue(matrix[row], target)

    def getValue(self, matrix, target):
        l, r = 0, len(matrix) - 1
        while l + 1 < r:
            mid = (l + r) / 2
            if matrix[mid] < target:
                l = mid
            else:
                r = mid
        if matrix[l]  == target or matrix[r] == target:
            return True
        else:
            return False


if __name__ == "__main__":
    matrix = [[-10,-8,-6,-4,-3],[0,2,3,4,5],[8,9,10,10,12]]
    # matrix = [[]]
    # matrix = [[-1, 0, 3, 4]]
    target = 0
    test = Solution().searchMatrix(matrix, target)
    print test