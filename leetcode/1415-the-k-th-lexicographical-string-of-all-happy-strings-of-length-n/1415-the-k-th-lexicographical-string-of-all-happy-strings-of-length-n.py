class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []
        lis = ['a', 'b', 'c']
        def backtrack(i, sub):
            if len(sub) == n:
                res.append("".join(sub))
                return
            for j in range(len(lis)):
                if j == i:
                    continue
                sub.append(lis[j])
                backtrack(j, sub)
                sub.pop()
        backtrack(-1, [])
        return res[k-1] if k <= len(res) else ""
