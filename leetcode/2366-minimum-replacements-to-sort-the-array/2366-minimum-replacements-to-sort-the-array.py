class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        last = nums[-1]
        res = 0
        for i in range(len(nums)-1, -1, -1):
            k = 1
            if nums[i] > last:
                k = ceil(nums[i] / last)
                res += k - 1
            last = nums[i] // k
        return res