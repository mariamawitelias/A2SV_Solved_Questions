class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid) , len(grid[0])
        memo = [[-1] * len(grid[0]) for _ in range(len(grid))]
        def dp(i, j):
            if i == m-1 and j == n-1:
                return grid[i][j]
            if memo[i][j] == -1:
                if i == m - 1:
                    memo[i][j] = grid[i][j] + dp(i, j+1)
                elif j == n-1:
                    memo[i][j] = grid[i][j] + dp(i+1, j)
                else:
                    memo[i][j] = grid[i][j] + min(dp(i+1, j), dp(i, j+1))
            return memo[i][j] 
        return dp(0, 0)
