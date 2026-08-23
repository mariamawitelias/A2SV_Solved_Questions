class Solution:
    def minSteps(self, n: int) -> int:
        memo = {}
        def dp(count, paste):
            if count == n:
                return 0
            if count > n:
                return 1000
            if (count, paste) in memo:
                return memo[(count, paste)]
            res1 = 1 + dp(count+paste, paste)
            res2 = 2 + dp(count+count, count)
            memo[(count, paste)] = min(res1, res2)
            return memo[(count, paste)]
        if n == 1:
            return 0
        return 1 + dp(1,1)