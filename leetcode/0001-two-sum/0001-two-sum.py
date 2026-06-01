class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp = {}
        for i, value in enumerate(nums):
            x = target - value
            if x in mapp:
                return [i, mapp[x]]
            else: 
                mapp[value] = i
        