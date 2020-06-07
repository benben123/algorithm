class IsParlindrome:
    def isParlindrome(self, num):
        div = 1
        while num/div >=10:
            div *= 10
        while num>=10:
            right = num % 10
            left = num / div
            if left != right:
                return False
            num = num % div /10
            div = div/100
        return True

    def isParlin2(self, num):
        string = str(num)
        length = len(string)
        left, right = 0, length - 1
        while left < right:
            if string[left] == string[right]:
                left += 1
                right -= 1
            else:
                return False
        return True

if __name__ == "__main__":
    test = IsParlindrome()
    a = test.isParlindrome(2343)
    b = test.isParlin2(2223)
    print a, b
