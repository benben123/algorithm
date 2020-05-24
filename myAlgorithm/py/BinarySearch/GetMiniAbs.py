class getMiniAbs:
    def getMiniAbs(self, arr):
        if not arr:
            return None
        l, r = 0, len(arr) -1
        while l + 1 < r:
            mid = (l + r)/2
            if abs(arr[mid - 1]) < abs(arr[mid]):
                r = mid
            else:
                l = mid
        if abs(arr[l]) < abs(arr[r]):
            return arr[l]
        else:
            return arr[r]


if __name__ == "__main__":
    arr1 = [-4, -2, 0, 2, 4]
    arr2 = [-4, -2, -1, 0.5, 4]
    arr3 = [-4, -2]
    arr4 = [0]
    arr5 = [1, 2, 3, 4]
    arr6 = [-4, -3, 3, 4]
    test = getMiniAbs()
    print test.getMiniAbs(arr1)
    print test.getMiniAbs(arr2)
    print test.getMiniAbs(arr3)
    print test.getMiniAbs(arr4)
    print test.getMiniAbs(arr5)
    print test.getMiniAbs(arr6)