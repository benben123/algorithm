def bsf(root):
    if root is None:
        return 0
    height = 0
    q = []
    q = [root]
    while 1:
        nodeCount = len(q)
        if nodeCount == 0:
            return height
        height = height + 1
        while nodeCount > 0:
            node = q.pop(0)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            nodeCount -= 1
    return height


def bsf2nd(root):
    thisLevel = [root]
    while thisLevel:
        nextLevel = list()
        for ele in thisLevel:
            print ele.val
            if ele.left:
                nextLevel.append(ele.left)
            if ele.right:
                nextLevel.append(ele.right)
        thisLevel = nextLevel



