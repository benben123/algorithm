class Solution:
    def isBST(self, root):
        return self.help(root, -float('inf'), float('inf'))

    def help(self, root, low, high):
        if root is None:
            return True
        return root.val < high and root.val > low \
               and self.help(root.left, low, root.val) \
               and self.help(root.right, root.val, high)