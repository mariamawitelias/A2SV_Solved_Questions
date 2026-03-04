class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        hashh = {0:1}
        pre = 0
        res = 0
        for i in range(len(nums)):
            pre += nums[i]
            res += hashh.get(pre-goal, 0)
            hashh[pre] = hashh.get(pre, 0) + 1
        return res
    
