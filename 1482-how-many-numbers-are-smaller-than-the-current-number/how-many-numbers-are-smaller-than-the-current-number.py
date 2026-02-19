class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        first_index = {}
        result = []
        arr = sorted(nums)
        print(arr)
        for i, val in enumerate(arr):
            if val not in first_index:
                first_index[val] = i
        for num in nums:
            result.append(first_index[num])
        return result
        
        