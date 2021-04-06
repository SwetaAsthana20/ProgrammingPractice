def climbStairs(n: int) -> int:
    dp = [0, 1, 2, 3] + [0] * (n - 3)
    i = 4
    while i <= n:
        dp[i] = dp[i - 1] + dp[i - 2]
        i += 1

    return dp[n]


print(climbStairs(5))
