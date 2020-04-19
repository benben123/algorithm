"""
minimum subtree
https://www.lintcode.com/problem/minimum-subtree/description
Description
中文

English
Given a binary tree, find the subtree with minimum sum. Return the root of the subtree.
LintCode will print the subtree which root is your return node.
It's guaranteed that there is only one subtree with minimum sum and the given binary tree is not an empty tree.
Have you met this question in a real interview?  Yes
Problem Correction
Example
Example 1:

Input:
{1,-5,2,1,2,-4,-5}
Output:1
Explanation:
The tree is look like this:
     1
   /   \
 -5     2
 / \   /  \
1   2 -4  -5
The sum of whole tree is minimum, so return the root.
Example 2:

Input:
{1}
Output:1
Explanation:
The tree is look like this:
   1
There is one and only one subtree in the tree. So we return 1.

"""

class MinimumSubtree:
    def getMiniSubtreee(self, root):
        self.miniVal = float('inf')   # 作为全局变量
        self.node = None
        # 调用help 函数，但返回在函数内部，用全局变量来记录最小值，然后返回
        self.help(root)
        return self.node

    def help(self, root):
        if not root:
            return 0
        left = self.help(root.left)
        right = self.help(root.right)
        sumVal = left + right + root.val
        if self.miniVal > sumVal:
            self.miniVal = sumVal
            self.node = root
        return sumVal