class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dp(n):
            if n == 0: 
                return 0
            if n < 0:
                return -1
            if n in memo:
                return memo[n]
            mini = float("inf")
            for coin in coins:
                res = dp(n-coin)
                if res != -1:
                    mini = min(mini, 1+res)
            memo[n] = mini if mini != float("inf") else -1
            return memo[n]
        return dp(amount)
            