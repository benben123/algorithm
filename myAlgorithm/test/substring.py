def issubstring(s1, s2):
    length1= len(s1)
    length2= len(s2)
    i, j = 0, 0
    while i < length1:
        while s1[i] != s2[j] and j <length2:
            j += 1
        if s1[i] == s2[j]:
            i += 1
            j += 1
        if j == length2:
            return False
        if i == length1:
            return True

        