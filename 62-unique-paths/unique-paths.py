class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = []
        for i in range(m):
            memo.append([-1] * n)
        direction = [(0, 1), (1, 0)]
        def dp(i, j):
            if i == 0 and j == 0:
                return 1
            if i < 0 or j < 0:
                return 0
            if memo[i][j] == -1:
                up = dp(i-1, j)
                left = dp(i, j-1)
                memo[i][j] = up+left
            return memo[i][j]
        return dp(m-1, n-1)