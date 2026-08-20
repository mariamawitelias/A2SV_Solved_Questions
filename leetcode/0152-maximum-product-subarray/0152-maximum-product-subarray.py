class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        dp_max = [0] * n
        dp_min = [0] * n

        dp_max[0] = nums[0]
        dp_min[0] = nums[0]

        answer = nums[0]

        for i in range(1, n):
            num = nums[i]

            dp_max[i] = max(
                num,
                num * dp_max[i - 1],
                num * dp_min[i - 1]
            )

            dp_min[i] = min(
                num,
                num * dp_max[i - 1],
                num * dp_min[i - 1]
            )

            answer = max(answer, dp_max[i])

        return answer