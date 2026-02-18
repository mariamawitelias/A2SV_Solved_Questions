class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        for i in range(1, len(nums)-1):
            res = nums[i-1]
            if res < nums[i] + nums[i+1]:
                res += nums[i] + nums[i+1]
                return res
        return 0




        