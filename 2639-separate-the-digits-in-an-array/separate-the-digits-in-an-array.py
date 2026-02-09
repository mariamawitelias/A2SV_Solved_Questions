class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            x = str(i)
            for j in x:
                res.append(int(j))
        return res
        