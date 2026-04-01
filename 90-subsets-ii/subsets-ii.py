class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(i, sub):
            if i == len(nums):
                res.append(sub[:])
                return
            sub.append(nums[i])
            backtrack(i+1, sub)   
            sub.pop()
            while i+1 < len(nums) and nums[i+1] == nums[i]:
                i += 1
            backtrack(i+1, sub)
        backtrack(0, [])
        return res