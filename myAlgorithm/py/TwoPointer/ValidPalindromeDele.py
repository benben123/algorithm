"""
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
"""
class Solution:

    def checkPalindrome(self, str):
        result = self.checkPalindrome2(str)
        if result == True:
            return True
        else:
            start = result[0]
            end = result[1]
            checkLeft = self.checkPalindrome2(str[start+1:end+1])
            checkRight = self.checkPalindrome2(str[start:end])
            if checkLeft == True or checkRight == True:
                return True
            else:
                return False

    def checkPalindrome2(self,str):
        start, end = 0, len(str)-1
        while start < end and str[start] == str[end]:
            start += 1
            end -= 1
        if start >= end:
            return True
        else:
            return [start, end]


if __name__ == '__main__':
    str = 'abdbfca'
    test = Solution().checkPalindrome(str)
    print test
