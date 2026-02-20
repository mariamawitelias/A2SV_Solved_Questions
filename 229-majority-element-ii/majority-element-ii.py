class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        a = len(nums) / 3
        res = []
        for k, v in count.items():
            if v > a:
                res.append(k)
        return res




        