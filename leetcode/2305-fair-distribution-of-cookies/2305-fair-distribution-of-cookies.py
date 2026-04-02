class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        child = [0] * k
        self.res = float('inf')
        def backtrack(i, child):
            if i >= len(cookies):
                self.res = min(self.res, max(child))
                return
            if max(child) > self.res:
                return
            for j in range(k):
                child[j] += cookies[i]
                backtrack(i+1, child)
                child[j] -= cookies[i]
        backtrack(0, child)
        return self.res