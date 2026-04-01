class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []
        lis = ['a', 'b', 'c']
        count = [0]
        sub = []
        def backtrack(i):
            if len(sub) == n:
                count[0] += 1
                return
            for j in range(len(lis)):
                if j == i:
                    continue
                sub.append(lis[j])
                backtrack(j) 
                if count[0] == k:
                    return
                sub.pop()
        backtrack(-1)
        return "".join(sub)
