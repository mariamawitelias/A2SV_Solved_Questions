class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        x = int(len(nums) / 3)
        count = Counter(nums)
        res = []
        for key, value in count.items():
            if value > x:
                res.append(key)
        return res



        