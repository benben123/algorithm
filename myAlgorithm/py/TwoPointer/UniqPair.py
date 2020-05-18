class UniqPair:
    def uniqPair(self, lst, tar):
        lst.sort()
        left, right = 0, len(lst) - 1
        count = 0
        while left < right:
            if lst[left] + lst[right] >tar:
                right -= 1
            elif lst[left] + lst[right] <tar:
                left += 1
            else:
                count += 1
                left += 1
                right -= 1
                while left < right and lst[left] == lst[left-1]:
                    left += 1
                while left < right and lst[right] == lst[right + 1]:
                    right -= 1
        return count
