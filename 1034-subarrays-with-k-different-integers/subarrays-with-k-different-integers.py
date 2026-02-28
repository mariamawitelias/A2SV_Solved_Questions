class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        wind = {}
        count = 0
        l, j = 0, 0
        res = 0
        for r in range(len(nums)):
            wind[nums[r]] = wind.get(nums[r], 0) + 1
            while len(wind) > k:
                wind[nums[l]] -= 1
                if wind[nums[l]] == 0:
                    del wind[nums[l]]
                l += 1
                j = l
            while l < len(nums) and wind[nums[l]] > 1:
                wind[nums[l]] -= 1
                l += 1
            if len(wind) == k:
                res += l - j + 1
        return res