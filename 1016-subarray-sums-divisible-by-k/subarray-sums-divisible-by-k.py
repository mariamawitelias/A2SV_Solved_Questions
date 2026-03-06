class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        table = {0:1}
        pre = 0
        res = 0
        for i in range(len(nums)):
            pre += nums[i]
            remain = pre % k
            res += table.get(remain, 0)
            table[remain] = table.get(remain, 0) + 1
        return res