class Solution:
    def lastRemaining(self, n: int) -> int:
        def recur(n, left):
            if n == 1:
                return 1
            if left:
                return 2 * recur(n // 2, False)
            else:
                if n % 2 == 1:
                    return 2 * recur(n // 2, True)
                else:
                    return 2 * recur(n // 2, True) - 1
        return recur(n, True)
            