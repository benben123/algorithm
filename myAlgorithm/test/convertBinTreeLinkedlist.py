class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def binaryTreeToLists(self, root):
        res = []
        cur = [root]
        dummy = ListNode(0)
        lastNode = None
        while cur:
            dummy.next = None
            lastNode = dummy
            length = len(cur)
            for i in range(length):
                node = cur.pop()
                lastNode.next = ListNode(node.val)
                lastNode = lastNode.next

                if node.left:
                    cur.append(node.left)
                if node.right:
                    cur.append(node.right)
            res.append(dummy.next)
        return res
