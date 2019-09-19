def dp(p, n):
    if n == 0:
        return 0
    q = float('-inf')
    for i in range(1,n+1):
        q = max(q, dp(p, n-1))
    return q
