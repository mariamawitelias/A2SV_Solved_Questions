class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        table = {0:-1}
        cur = 0
        res = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cur += 1
            else:
                cur -= 1
            if cur in table:
                res = max(res, i - table[cur])
            else:
                table[cur] = i
        return res
