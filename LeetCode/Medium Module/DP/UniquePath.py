def uniquePaths(m: int, n: int) -> int:
    dp = [[-1 for i in range(n)] for j in range(m)]
    def get_paths(i, j):
        if i == m - 1 and j == n - 1:
            return 1
        elif i >= m or i < 0 or j < 0 or j >= n:
            return 0
        else:
            if i < m and i >= 0 and j >= 0 and j < n and dp[i][j] != -1:
                return dp[i][j]
            else:
                dp[i][j] = get_paths(i+1,j) + get_paths(i,j+1)
                return dp[i][j]

    return get_paths(0, 0)


print(uniquePaths(3, 7))