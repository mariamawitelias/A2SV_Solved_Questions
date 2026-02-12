class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        prev = 0
        total = 0
        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            num = roman[ch]
            if num < prev:
                total -= num
            else:
                total += num
            prev = num
        return total
        
