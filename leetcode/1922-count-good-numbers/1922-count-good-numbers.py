class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        def pow(x, n):
            def recur(x, n):
                if n == 0:
                    return 1
                if x == 0:
                    return 0
                res = recur((x*x)%MOD, n//2)
                return res * x if n % 2 == 1 else res
            ans = recur(x, abs(n))
            return ans if n >= 0 else 1 / ans
        even = ceil(n / 2)
        odd = n // 2
        return (pow(5, even) * pow(4, odd)) % MOD

        