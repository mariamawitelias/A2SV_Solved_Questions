class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def checker(candy):
            lijoch = 0
            for pile in candies:
                lijoch += pile // candy
            return lijoch >= k
        
        l, r = 1, max(candies)
        while l <= r:
            mid = (l + r) // 2
            if checker(mid) == True:
                l = mid + 1
            else:
                r = mid - 1
        return r