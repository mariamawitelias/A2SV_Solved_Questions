class Solution(object):
    def minSubArrayLen(self, target, nums):
        window = 0
        l = 0
        res = float('inf')
        for r in range(len(nums)):
            window += nums[r]
            while window >= target:
                res = min(res, r -l + 1)
                window -= nums[l]
                l += 1
        return 0 if res == float('inf') else res
