class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mp = {}
        start, end = 0, 0
        res = []
        for i, char in enumerate(s):
            mp[char] = i
        for i in range(len(s)):
            end = max(end, mp[s[i]])
            if i == end:
                res.append(end - start + 1)
                start = i + 1
        return res

        

        