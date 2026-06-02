class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        memo = [[None] * n for _ in range(n)]

        def dp(l, r):
            if l >= r:
                return True

            if memo[l][r] is not None:
                return memo[l][r]

            memo[l][r] = s[l] == s[r] and dp(l + 1, r - 1)
            return memo[l][r]

        start, maxi = 0, 1
        for i in range(n):
            for j in range(i, n):
                if dp(i, j) and j - i + 1 > maxi:
                    maxi = j - i + 1
                    start = i

        return s[start:start + maxi]