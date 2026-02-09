class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        table = {}
        for x, y in zip(s, indices):
            table[y] = x
        res = ""
        for i in range(len(s)):
            res += table[i]
        return res