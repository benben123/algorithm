# Binary Tree Level Order Traversal

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return None
        res, cur = [], []
        cur.append(root)
        while 1:
            level, val = [], []
            for node in cur:
                val.append(node.val)
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            cur = level
            res.append(val)
            if not level:
                break
        return res
