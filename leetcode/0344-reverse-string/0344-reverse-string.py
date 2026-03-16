class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def recur(l, r):
            if l >= r:
                return 1
            s[l], s[r] = s[r], s[l]
            recur(l+1, r-1)
        recur(0, len(s)-1)
        