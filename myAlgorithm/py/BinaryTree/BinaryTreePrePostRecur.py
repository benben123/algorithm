class Traverse:
    def inorderTrav(self, root):
        self.res = []
        self.helpInorder(root)
        return self.res

    def helpInorder(self, root):
        if not root:
            return None
        self.helpInorder(root.left)
        self.res.append(root.val)
        self.helpInorder(root.right)

    def preOrderTrav(self, root):
        self.res = []
        self.helpPreorder(root)
        return self.res

    def helpPreorder(self, root):
        if not root:
            return None
        self.res.append(root.val)
        self.helpPreorder(root.left)
        self.helpPreorder(root.right)

    def postOrderTrav(self, root):
        self.res = []
        self.helpPostorder(root)
        return self.res

    def helpPosorder(self, root):
        if not root:
            return None
        self.helpPosorder(root.left)
        self.helpPosorder(root.right)
        self.res.append(root.val)