class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def dp(i, j):
            if i >= len(text1):
                return 0
            if j >= len(text2):
                return 0
            take = 0
            if (i, j) not in memo:
                for nj in range(j, len(text2)):
                    if text1[i] == text2[nj]:
                        take = 1 + dp(i+1, nj+1)
                        break
                notake = dp(i+1, j)
                memo[(i, j)] = max(take, notake)
            return memo[(i, j)]
        return dp(0, 0)