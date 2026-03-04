class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix = 0
        res = nums[0]
        for n in nums:
            if prefix < 0:
                prefix = 0
            prefix += n
            res = max(res, prefix)
        return res

