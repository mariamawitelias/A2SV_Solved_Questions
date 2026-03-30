class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(i, comb):
            if len(comb) > 1:
                res.append(comb[:])
            if i == len(nums):
                return
            exist = set()
            for j in range(i, len(nums)):
                if nums[j] in exist:
                    continue
                if comb:
                    if nums[j] < comb[-1]:
                        continue
                comb.append(nums[j])
                exist.add(nums[j])
                backtrack(j+1, comb)
                comb.pop()
        backtrack(0, [])
        res.sort()
        return res
                
                    