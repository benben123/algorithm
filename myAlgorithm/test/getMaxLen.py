def getMaxLen(num):
    maxLen, count = 0, 1
    for i in range(len(num)):
        start = num[i]
        for j in range(i, len(num)):
            if start < num[j]:
                count += 1
                start = num[j]
        maxLen = max(maxLen, count)
        count = 1
    return maxLen


if __name__ == "__main__":
    # num = [1, 2, 4, 2, 7]
    num = [10, 2, 10, 3, 5]
    print getMaxLen(num)
