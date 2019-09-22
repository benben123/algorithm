# Get unique number of paths on m*n grid

# Backtracking
def getUniqueNumbers(m, n):
    return backTrack(0, 0, m, n)


def backTrack(r, l, m, n):
    if r == m - 1 and l == n - 1:
        return 1
    if r >= m or l >= n:
        return 0
    return backTrack(r+1, l, m, n) + backTrack(r, l+1, m, n)


# DP method
def dpgetUnique(m, n):
    val = [[-1 for i in range(m+1)] for j in range(n+1)]
    return getDPVal(val, 0, 0, m, n)


def getDPVal(val, l, r, m, n):
    if l == m - 1 and r == n - 1:
        return 1
    if l >= m or r >= n:
        return 0
    if val[r+1][l] == -1:
        val[r+1][l] = getDPVal(val, l, r+1, m, n)
    if val[r][l+1] == -1:
        val[r][l+1] = getDPVal(val, l+1, r, m, n)
    return val[r+1][l] + val[r][l+1]


# from bottom to up
def getMethod(m, n):
    mat = [[0 for i in range(m+1)] for j in range(n+1)]
    mat[n-1][m] = 1
   # mat[n][m-1] = 1
    for l in reversed(range(n)):
        for r in reversed(range(m)):
            mat[l][r] = mat[l+1][r] + mat[l][r+1]
    return mat[0][0]


# Unique Path with obstacles
def getWithObsNumber(obst):
    m = len(obst)
    if m == 0:
        return 0
    n = len(obst[0])
    mat = [[0 for i in range(n+1)] for j in range(m+1)]
    mat[m-1][n] = 1
    for r in reversed(range(m)):
        for l in reversed(range(n)):
            if obst[r][l] == 1:
                mat[r][l] = 0
            else:
                mat[r][l] = mat[r+1][l] + mat[r][l+1]
    return mat[0][0]

if __name__ == '__main__':

    # print getUniqueNumbers(3, 4)
    # print dpgetUnique(3, 4)
    # print getMethod(2, 2)
    obst = [[0, 0, 0], [0, 1, 0]]
    print getWithObsNumber(obst)