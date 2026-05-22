class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        def dp(arr):

            if len(arr) == 1:
                return arr[0]

            memo = [0] * len(arr)

            memo[0] = arr[0]
            memo[1] = max(arr[0], arr[1])

            for i in range(2, len(arr)):
                memo[i] = max(
                    memo[i-1],
                    memo[i-2] + arr[i]
                )

            return memo[-1]

        return max(
            dp(nums[:-1]),
            dp(nums[1:])
        )