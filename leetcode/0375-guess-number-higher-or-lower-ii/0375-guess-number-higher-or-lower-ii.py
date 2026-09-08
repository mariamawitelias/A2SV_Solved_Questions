class Solution:
    def getMoneyAmount(self, n: int) -> int:
        def dp(i, j, memo: dict):
            if i >= j:
                return 0
            if (i, j) not in memo:
                memo[(i, j)] = float('inf')
                for x in range(i, j+1):
                    lower = dp(i, x-1, memo)
                    higher = dp(x+1, j, memo)
                    memo[(i, j)] = min(memo[(i, j)], x + max(lower, higher))
            return memo[(i, j)]
        return dp(1, n, {})