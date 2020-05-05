"""
Closest Binary Search Tree Value
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.
Example1

Input: root = {5,4,9,2,#,8,10} and target = 6.124780
Output: 5
Explanation：
Binary tree {5,4,9,2,#,8,10},  denote the following structure:
        5
       / \
     4    9
    /    / \
   2    8  10
Example2

Input: root = {3,2,4,1} and target = 4.142857
Output: 4
Explanation：
Binary tree {3,2,4,1},  denote the following structure:
     3
    / \
  2    4
 /
1
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class ClosetBST:
    def getClosest(self, root, k):
        upper, lower = -float("inf"), float("inf")
        while root:
            if root.val <= k:
                lower = root.val
                root = root.right
            else:
                upper = root.val
                root = root.left
        if abs(upper - k) <= abs(lower - k):
            return upper
        else:
            return lower


if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(20)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(8)
    root.right.left = TreeNode(12)

    test = ClosetBST().getClosest(root, 0)
    print test