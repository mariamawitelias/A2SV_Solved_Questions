class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r
        def check(cap):
            curr, ship = cap, 1
            for w in weights:
                if curr - w < 0:
                    ship += 1
                    curr = cap
                curr -= w
            return ship <= days
        while l <= r:
            cap = (l+r) // 2
            if check(cap):
                res = min(res, cap)
                r = cap - 1
            else:
                l = cap + 1
        return res

        
            
            