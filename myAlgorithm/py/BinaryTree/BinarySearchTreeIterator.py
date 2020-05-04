"""
Design an iterator over a binary search tree with the following rules:

Elements are visited in ascending order (i.e. an in-order traversal)
next() and hasNext() queries run in O(1) time in average.

Input:  {10,1,11,#,6,#,12}
Output:  [1, 6, 10, 11, 12]
Explanation:
The BST is look like this:
  10
  /\
 1 11
  \  \
   6  12
You can return the inorder traversal of a BST [1, 6, 10, 11, 12]

NOTE: Similar to KthSmallBST, both using in order traverse
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right, self.left = None, None

class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self.curt = root

    def hasNext(self):
        return self.curt is not None or len(self.stack) > 0

    def next(self):
        while self.curt:
            self.stack.append(self.curt)
            self.curt = self.curt.left
        self.curt = self.stack.pop()
        next = self.curt
        self.curt = self.curt.right
        return next
