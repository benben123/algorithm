class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def isBalancedTree(self, root):
        if not root:
            return True
        if abs(self.getHight(root.left) - self.getHight(root.right)) <= 1:
            return self.isBalancedTree(root.left) and self.isBalancedTree(root.right)
        else:
            return False

    def getHight(self, root):
        if not root:
            return 0
        return max(self.getHight(root.left), self.getHight(root.right)) + 1