class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        memo = [[-1 for _ in range(2)] for _ in range(n)]
        def dp(i, bought):
            if i >= n:
                return 0
            res = 0
            if memo[i][bought] != -1:
                return memo[i][bought]

            if not bought:
                buy = dp(i+1, True) - prices[i]
                skip = dp(i+1, False)
                res = max(buy, skip)
            else:
                sell = dp(i+1, False) + prices[i] - fee
                skips = dp(i+1, True)
                res = max(sell, skips) 
            memo[i][bought] = res
            return res
        return dp(0, False)