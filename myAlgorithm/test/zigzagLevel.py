class BTree:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return None
        res = []
        cur = [root]
        level = 0
        while cur:
            level += 1
            val, cur_temp = [], []
            while cur:
                node = cur.pop()   # 对于要左右互换的情况，可以采用pop，否则用for
                val.append(node.val)
                if level % 2 == 1:
                    if node.left:
                        cur_temp.append(node.left)
                    if node.right:
                        cur_temp.append(node.right)
                if level % 2 == 0:
                    if node.right:
                        cur_temp.append(node.right)
                    if node.left:
                        cur_temp.append(node.left)
            res.append(val)
            cur = cur_temp
        return res


if __name__ == "__main__":
    root = BTree(1)
    root.left = BTree(2)
    root.right = BTree(3)
    root.left.left = BTree(4)
    root.right.right = BTree(5)

    test = Solution().zigzagLevelOrder(root)
    print test