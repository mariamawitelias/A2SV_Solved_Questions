class Solution:
    def findValidPair(self, s: str) -> str:
        count = Counter(s)
        for i in range(1, len(s)):
            if s[i-1] != s[i] and int(s[i -1]) == count[s[i-1]] and int(s[i]) == count[s[i]]:
                return s[i-1] + s[i]
        return ""


        