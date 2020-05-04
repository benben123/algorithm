"""
Invert Binary Tree
Easy

Add to List

Share
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""
class Solution:
    def invertBT(self, root):
        if root is None:
            return
        self.invertBT(root.left)
        self.invertBT(root.right)
        root.left, root.right = root.right, root.left
        return root
