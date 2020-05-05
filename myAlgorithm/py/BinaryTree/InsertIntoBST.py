"""
Given the root node of a binary search tree (BST) and a value to be inserted into the tree, insert the
value into the BST. Return the root node of the BST after the insertion. It is guaranteed that the new
value does not exist in the original BST.

Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after
insertion. You can return any of them.

For example,

Given the tree:
        4
       / \
      2   7
     / \
    1   3
And the value to insert: 5
You can return this binary search tree:

         4
       /   \
      2     7
     / \   /
    1   3 5
This tree is also valid:

         5
       /   \
      2     7
     / \
    1   3
         \
          4

Note: for inserting into BST, I had misunderstanding before, it was not to cut some branch and re-build the tree, it is
about to add the new node at the end of right point

"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class InsertIntoBST:
    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val)
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root

    def insertIntoBSTNotRecur(self, root, val):
        if not root:
            return TreeNode(val)
        cur = root
        while True:
            if cur.val < val:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = TreeNode(val)
                    break
            else:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = TreeNode(val)
                    break
        return root
