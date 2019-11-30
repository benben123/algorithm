def longestSubString(lst):
    lstRd = []
    MaxLen = 0
    for i in range(len(lst)):
        while lst[i] in lstRd:
            lstRd.pop()
        lstRd.append(lst[i])
        MaxLen = max(MaxLen, len(lstRd))
    return MaxLen



if __name__ == '__main__':
    lst = ['a', 'b', 'c', 'b', 'd', 'f', 'g']
    print longestSubString(lst)