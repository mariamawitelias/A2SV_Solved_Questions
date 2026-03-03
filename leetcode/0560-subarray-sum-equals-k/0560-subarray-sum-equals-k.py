class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        table = {0:1}
        pre = 0
        res = 0
        for i in range(len(nums)):
            pre += nums[i]
            res += table.get(pre-k, 0)
            table[pre] = table.get(pre, 0) + 1
        return res