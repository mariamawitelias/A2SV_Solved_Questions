class Solution:
    def arrangeCoins(self, n: int) -> int:
        def check(k):
            return k * (k + 1) // 2 <= n  
        l, r = 0, n
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
        return r