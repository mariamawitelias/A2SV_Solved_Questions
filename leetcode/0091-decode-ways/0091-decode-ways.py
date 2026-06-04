class Solution:
    def numDecodings(self, s: str) -> int:
        memo = [-1] * len(s)
        def dp(i):
            if i == len(s):
                return 1
            if memo[i] != -1:
                return memo[i]
            if s[i] == '0':
                return 0
            ans = dp(i + 1)
            if i + 1 < len(s) and (
                s[i] == '1' or
                (s[i] == '2' and s[i + 1] <= '6')
            ):
                ans += dp(i + 2)

            memo[i] = ans
            return ans
        return dp(0)