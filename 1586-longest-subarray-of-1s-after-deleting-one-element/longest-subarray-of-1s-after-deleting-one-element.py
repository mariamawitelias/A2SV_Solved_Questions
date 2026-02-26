class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        window = 0
        l = 0
        res = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                window += 1
            while window > 1:
                if nums[l] == 0:
                    window -= 1
                l += 1
            res = max(res, r - l)
        return res

        