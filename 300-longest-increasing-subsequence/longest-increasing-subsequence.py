class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [[-1] * (len(nums) + 1) for _ in range(len(nums))]
        def dp(i, last):
            if i == len(nums):
                return 0
            if memo[i][last] == -1:
                inc = 0
                if last == -1 or nums[last] < nums[i]:
                    inc = 1 + dp(i+1, i)
                memo[i][last] = max(inc, dp(i+1, last))
            return(memo[i][last])
        return dp(0, -1)