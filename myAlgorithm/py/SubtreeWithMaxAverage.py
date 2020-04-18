"""
https://www.lintcode.com/problem/subtree-with-maximum-average/description
Description
中文

English
Given a binary tree, find the subtree with maximum average. Return the root of the subtree.
LintCode will print the subtree which root is your return node.
It's guaranteed that there is only one subtree with maximum average.
Have you met this question in a real interview?  Yes
Problem Correction
Example
Example 1

Input：
{1,-5,11,1,2,4,-2}
Output：11
Explanation:
The tree is look like this:
     1
   /   \
 -5     11
 / \   /  \
1   2 4    -2
The average of subtree of 11 is 4.3333, is the maximun.
Example 2

Input：
{1,-5,11}
Output：11
Explanation:
     1
   /   \
 -5     11
The average of subtree of 1,-5,11 is 2.333,-5,11. So the subtree of 11 is the maximum

*******note:
1. 全局变量的使用
2. 递归呀递归

"""
class Solution:
    average = -float('inf')
    node = None

    def findSubtree(self, root):
        self.helper(root)
        return self.node

    def helper(self, root):
        if not root:
            return 0, 0
        left_sum, left_size = self.helper(root.left)
        right_sum, right_size = self.helper(root.right)

        sum, size = left_sum + right_sum + root.val, left_size + right_size + 1
        if not self.node or sum*1.0/size > self.average:
            self.node = root
            self.average = sum*1.0/size
        return sum, size