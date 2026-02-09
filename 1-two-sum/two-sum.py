class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i, value in enumerate(nums):
            x = target - value
            if x in table:
                return [i, table[x]]
            else: 
                table[value] = i
        