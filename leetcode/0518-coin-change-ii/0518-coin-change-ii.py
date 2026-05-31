class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dp(i, rem):
            if rem == amount:
                return 1
            if rem > amount:
                return 0
            if i == len(coins):
                return 0
            if (i, rem) in memo:
                return memo[(i, rem)]
            memo[(i, rem)] = dp(i, rem + coins[i]) + dp(i+1, rem)
            return memo[(i, rem)]
        return dp(0, 0)             
            
