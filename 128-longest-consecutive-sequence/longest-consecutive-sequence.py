class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set(nums)
        longest = 0
        for i in num:
            if i - 1 not in num:
                len = 0
                while (i + len) in num:
                    len += 1
                longest = max(longest, len)
        return longest