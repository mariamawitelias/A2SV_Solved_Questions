class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        k = n >> 2
        c0 = s.count('Q')
        c1 = s.count('W')
        c2 = s.count('E')
        c3 = n - c0 - c1 - c2
        if c0 <= k and c1 <= k and c2 <= k and c3 <= k:
            return 0
        res = n
        left = 0
        for right in range(n):
            ch = s[right]
            if ch == 'Q': c0 -= 1
            elif ch == 'W': c1 -= 1
            elif ch == 'E': c2 -= 1
            else: c3 -= 1
            while c0 <= k and c1 <= k and c2 <= k and c3 <= k:
                w = right - left + 1
                if w < res:
                    res = w
                ch = s[left]
                if ch == 'Q': c0 += 1
                elif ch == 'W': c1 += 1
                elif ch == 'E': c2 += 1
                else: c3 += 1
                left += 1
        return res                                                                                                                                                                                                                                                                                                                                