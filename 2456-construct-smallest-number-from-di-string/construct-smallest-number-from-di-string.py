class Solution:
    def smallestNumber(self, pattern: str) -> str:
        nums = list(range(1, len(pattern) + 2))  
        res = ["9" * (len(pattern) + 1)] 
        used = [False] * len(nums)
        def backtrack(comb):
            if len(comb) == len(nums):
                candidate = "".join(map(str, comb))
                if candidate < res[0]:
                    res[0] = candidate
                return
            for j in range(len(nums)):
                if used[j]:
                    continue
                if comb:
                    i = len(comb) - 1
                    if pattern[i] == 'I' and comb[-1] >= nums[j]:
                        continue
                    if pattern[i] == 'D' and comb[-1] <= nums[j]:
                        continue
                used[j] = True
                comb.append(nums[j])
                backtrack(comb)
                comb.pop()
                used[j] = False
        backtrack([])
        return res[0]