class Solution:
    def maxDistance(self, poss: List[int], m: int) -> int:
        poss.sort()
        def checker(dif):
            yene = 0
            prev = float('-inf')
            for pos in poss:
                if pos - prev >= dif:
                    yene += 1
                    prev = pos
            return yene >= m
        l, r = 1, max(poss) - min(poss)
        while l <= r:
            mid = (l + r) // 2
            if checker(mid) == True:
                l = mid + 1
            else:
                r = mid - 1
        return r