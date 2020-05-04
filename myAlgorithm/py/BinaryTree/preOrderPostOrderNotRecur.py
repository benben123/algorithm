class Traversal:
    def preOrder(self, root):
        stack = []
        res = []
        while stack or root:
            if root:
                res.append(root.val)
                stack.append(root.right)
                root = root.left
            else:
                root = stack.pop()
        return res

    def postOrder(self, root):
        stack = []
        res = []
        while stack or root:
            res.append(root.val)
            stack.append(root.left)
            root = root.right
        else:
            root = stack.pop()
        return res[::-1]

    def inorder(self, root):
        stack = []
        res =[]
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                res.append(root.val)
                root = root.right
        return res

