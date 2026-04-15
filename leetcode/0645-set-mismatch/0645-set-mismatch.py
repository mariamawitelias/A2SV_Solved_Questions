class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        res = []
        arr = [i for i in range(1, len(nums)+1)]
        nums = set(nums)
        for k, v in count.items():
            if v == 2:
                res.append(k)
        for i in arr:
            if i not in nums:
                res.append(i)
        return res