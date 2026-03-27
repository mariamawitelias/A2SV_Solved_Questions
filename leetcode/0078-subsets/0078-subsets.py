class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(i, comb):
            res.append(comb[:])
            for j in range(i, len(nums)):
                comb.append(nums[j])
                backtrack(j+1, comb)
                comb.pop()
        backtrack(0, [])
        return res