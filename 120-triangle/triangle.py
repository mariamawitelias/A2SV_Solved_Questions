class Solution:
    def minimumTotal(self, triangle):
        dp = triangle[-1].copy()
        for row in range(len(triangle) - 2, -1, -1):
            for i in range(len(triangle[row])):
                dp[i] = triangle[row][i] + min(dp[i], dp[i + 1])

        return dp[0]