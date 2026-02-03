class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)[::-1]
        return str(x) == y
        