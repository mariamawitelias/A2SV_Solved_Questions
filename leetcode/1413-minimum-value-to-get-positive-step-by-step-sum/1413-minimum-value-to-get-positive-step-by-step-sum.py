class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        pre = 0
        for i, n in enumerate(nums):
            pre += n
            nums[i] = pre
        mini = min(nums)
        if mini < 0:
            return abs(mini) + 1
        else:
            return 1
