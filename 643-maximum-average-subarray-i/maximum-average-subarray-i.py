class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window = sum(nums[:k])
        l = 0
        res = window
        for r in range(k, len(nums)):
            window -= nums[l]
            window += nums[r]
            res = max(res, window)
            l += 1
        return res / k


        