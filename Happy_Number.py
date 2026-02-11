class Solution:
    def isHappy(self, n: int) -> bool:
        def get(number):
            tot = 0
            for c in str(number):
                tot += (int(c) * int(c))
            return tot
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get(n)
        return n == 1

