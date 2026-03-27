class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(comb):
            if len(comb) == len(nums):
                res.append(comb[:])
                return
            for j in range(len(nums)):
                if nums[j] in comb:
                    continue
                comb.append(nums[j])
                backtrack(comb)
                comb.pop()
        backtrack([])
        return res