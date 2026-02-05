class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        x = Counter(nums)
        res = []
        for i in nums:
            if x[i] == 2:
                res.append(i)
        res = set(res)
        ans = list(res)
        return ans

        