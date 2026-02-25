class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        res = 0
        l = 0
        window = 0
        for r in range(len(s)):
            if s[r] != t[r]:
                window += abs(ord(s[r]) - ord(t[r]))
            while window > maxCost:
                window -= abs(ord(s[l]) - ord(t[l]))
                l += 1
            res = max(res, r - l + 1)
        return res
        