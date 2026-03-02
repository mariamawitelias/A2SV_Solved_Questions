class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        pre = 0
        for i in range(len(nums)):
            pre += nums[i]
            nums[i] = pre
        return nums