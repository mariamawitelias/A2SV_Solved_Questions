class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0 , len(height)-1
        ans = 1
        res = 0
        while i < j:
            ans = min(height[i], height[j]) * (j - i)
            res = max(res, ans)
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return res



        
            
        