class Solution:
    def reverse(self, x: int) -> int:
        sum = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            rem = x % 10
            sum = sum * 10 + rem
            x = x // 10

        sum *= sign
        
        if sum > 2**31 - 1 or sum < -2**31:
            return 0

        return sum