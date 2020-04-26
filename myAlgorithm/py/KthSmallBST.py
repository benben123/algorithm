"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
"""
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution():
    def kthSmallest(self, root, k):
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right

    def kthSmallestRe(self, root, k):
        self.k = k
        self.res = None
        self.help(root)
        return self.res

    def help(self, root):
        if not root:
            return
        self.help(root.left)
        self.k -=1
        if self.k == 0:
            self.res = root.val
            return
        self.help(root.right)




if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(1)
    # test = Solution().kthSmallest(root,6)
    test = Solution().kthSmallestRe(root, 6)
    print test