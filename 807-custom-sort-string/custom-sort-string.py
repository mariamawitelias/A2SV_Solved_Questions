class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)
        res = []
        for i in order:
            if i in s:
                while count[i] != 0:
                    res.append(i)
                    count[i] -= 1
        for i in s:
            if i not in res:
                while count[i] != 0:
                    res.append(i)
                    count[i] -= 1
        return "".join(res)
        