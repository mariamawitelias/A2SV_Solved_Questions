class Solution:
    def fib(self, n: int) -> int:
        memo = {}
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n not in memo:
            memo[n] = self.fib(n-1) + self.fib(n-2)
        return memo[n]