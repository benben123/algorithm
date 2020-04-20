class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """

    def binaryTreePaths(self, root):
        if root is None:
            return []

        result = []
        self.dfs(root, [str(root.val)], result)
        return result

    def dfs(self, node, path, result):
        if node.left is None and node.right is None:
            result.append('->'.join(path))
            return

        if node.left:
            path.append(str(node.left.val))
            self.dfs(node.left, path, result)
            path.pop()

        if node.right:
            path.append(str(node.right.val))
            self.dfs(node.right, path, result)
            path.pop()

if __name__== "__main__":
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.left.right = TreeNode(5)
    tree.right = TreeNode(3)

    test = Solution().binaryTreePaths(tree)
    print test