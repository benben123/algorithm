class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class InorderTras:
    def inorderTras(self, root):
        stack, res = [], []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res

    def inorderTrasRecurs(self, root):
        self.res = []
        self.help(root)
        return self.res

    def help(self, root):
        if not root:
            return None
        self.help(root.left)
        self.res.append(root.val)
        self.help(root.right)

if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(20)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(8)
    root.right.left = TreeNode(12)
    test = InorderTras().inorderTras(root)
    test2 = InorderTras().inorderTrasRecurs(root)
    print test
    print test2