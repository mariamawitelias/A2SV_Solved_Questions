class Solution:
    def myPow(self, x: float, n: int) -> float:
        def recur(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            res = recur(x, n // 2)
            res = res * res
            if n % 2 == 0:
                return res
            return res * x
        ans = recur(x, abs(n))
        if n < 0:
            return 1 / ans
        return ans

        
        