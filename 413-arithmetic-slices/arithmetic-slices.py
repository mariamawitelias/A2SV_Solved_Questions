# Pattern: Sliding Windows
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        count = 0 
        result = 0  
        diff = nums[1] - nums[0]  
        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == diff:  
                count += 1
                result += count
            else:
                diff = nums[i] - nums[i - 1]
                count = 0

        return result