class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        pre = [] 
        prefix, sufix = 0, 0
        suf = [] 
        res = [] 
        for n in nums:
            pre.append(prefix)
            prefix += n
        for i in range(len(nums)-1, -1, -1):
            suf.append(sufix)
            sufix += nums[i]
        x = suf[::-1]
        for i in range(len(nums)):
            res.append(abs(pre[i] - x[i]))
        return res


            
