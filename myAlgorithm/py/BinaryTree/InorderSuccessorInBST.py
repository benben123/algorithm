"""
Inorder Successor in BST
Given a binary search tree (See Definition) and a node in it, find the in-order successor of that node in the BST.

If the given node has no in-order successor in the tree, return null.
Example 1:

Input: {1,#,2}, node with value 1
Output: 2
Explanation:
  1
   \
    2
Example 2:

Input: {2,1,3}, node with value 1
Output: 2
Explanation:
    2
   / \
  1   3
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class InorderSuccessorInBST:
    def find(self, root, val):
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val == val and not root.right:
                if stack:
                    node = stack.pop()
                    return node.val
            if root.val == val and root.right:
                root = root.right
                while root:
                    stack.append(root)
                    root = root.left
                node = stack.pop()
                return node.val
            root = root.right
        return None


if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(20)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(8)
    root.right.left = TreeNode(12)

    test1 = InorderSuccessorInBST().find(root, 10)
    print test1





