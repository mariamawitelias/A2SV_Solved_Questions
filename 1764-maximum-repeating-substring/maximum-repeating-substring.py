class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        lw, ls = len(word), len(sequence)
        dp = [0] * (ls + 1)
        count = 0
        for i in range(lw, ls+1):
            if sequence[i-lw:i] == word:
                dp[i] = dp[i-lw] + 1
                count = max(count, dp[i])
        return count

