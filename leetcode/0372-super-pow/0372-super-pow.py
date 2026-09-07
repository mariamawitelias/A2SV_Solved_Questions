class Solution:
    def pow(self, x, n, MOD):
        ans = 1
        x %= MOD

        while n > 0:
            if n & 1:
                ans = (ans * x) % MOD

            x = (x * x) % MOD
            n >>= 1

        return ans

    def superPow(self, a: int, b: List[int]) -> int:

        if a == 1:
            return 1

        num = 0

        for val in b:
            num = (num * 10 + val) % 1140

        # b is positive, so remainder 0 means
        # the exponent is a positive multiple of 1140.
        if num == 0:
            num = 1140

        return self.pow(a, num, 1337)        