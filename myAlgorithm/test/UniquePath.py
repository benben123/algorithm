# Get unique number of paths on m*n grid

# Backtracking


def getUniqueNumbers(m, n):
    backTrack(0, 0, m, n)


def backTrack(r, l, m, n):
    if r == m - 1 and l == n - 1:
        return 1
    if r >= m or l >= n:
        return 0
    return backTrack(r+1, l, m, n) + backTrack(r, l+1, m, n)


# DP method


def dpgetUnique(m, n):
    val = [[ -1 for i in range(m)] for j in range(n)]
    getDPVal(val, 0, 0, m, n)


def getDPVal(val, l, r, m, n):
    if l == m - 1 and r == n - 1:
        return 1
    if l >= 0 or r >= 0:
        return 0
    if val[r+1][l] == -1:
        val[r+1][l] = getDPVal(val, l, r+1, m, n)
    if val[r][l+1] == -1:
        val[r][l+1] = getDPVal(val, l+1, r, m, n)
    return val[r+1][l] + val[r][l+1]


if __name__ == '__main__':
    dpgetUnique(1, 2)