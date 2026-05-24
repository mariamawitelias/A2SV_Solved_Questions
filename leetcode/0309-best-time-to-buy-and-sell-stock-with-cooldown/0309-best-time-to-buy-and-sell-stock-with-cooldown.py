class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        # memo[day][holding_status]
        memo = [[-1 for _ in range(2)] for _ in range(n)]

        def dp(i, bought):
            # Base Case: Out of days
            if i >= n:
                return 0

            # Check cache
            if memo[i][bought] != -1:
                return memo[i][bought]

            if not bought:
                # Option 1: Buy today
                buy = dp(i + 1, True) - prices[i]
                # Option 2: Skip buying today
                skip_buy = dp(i + 1, False)
                result = max(buy, skip_buy)
            else:
                # Option 1: Sell today (enforce 1-day cooldown with i + 2)
                sell = dp(i + 2, False) + prices[i]
                # Option 2: Skip selling today
                skip_sell = dp(i + 1, True)
                result = max(sell, skip_sell)

            memo[i][bought] = result
            return result

        return dp(0, False)