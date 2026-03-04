class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0] * len(s)
        res = ""
        for start, end, direction in shifts:
            if direction == 1:
                prefix[start] += 1
                if end + 1 < len(s):
                    prefix[end+1] -= 1
            else:
                prefix[start] -= 1
                if end + 1 < len(s):
                    prefix[end+1] += 1
        pre = 0
        for i in range(len(prefix)):
            pre += prefix[i]
            prefix[i] = pre
        for i in range(len(s)):
            shift = chr(((ord(s[i])-ord('a') + prefix[i]) % 26) + ord('a'))
            res += shift
        return res


        