class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dp(N):
            if N < 3:
                return N
            if N not in memo:
                memo[N] = dp(N-1)+ dp(N-2)
            return memo[N]
        return dp(n)
    