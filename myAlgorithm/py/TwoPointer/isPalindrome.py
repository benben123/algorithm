"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false

"""
class Solution:

    def isPalindrome2(self, s):
        """
        :type s: str
        :rtype: bool
        note: start < end is very important inside the second while loop
        """
        start, end = 0, len(s) - 1
        while start < end:
            while start < end and not s[start].isalpha() and not s[start].isdigit():
                start += 1
            while start < end and not s[end].isalpha() and not s[end].isdigit():
                end -= 1
            if s[start].lower() == s[end].lower():
                start += 1
                end -= 1
            else:
                return False
        return True


if __name__ == "__main__":
    lst = "A man, a plan, a canal: Panama"
    test = Solution().isPalindrome2(lst)
    print test