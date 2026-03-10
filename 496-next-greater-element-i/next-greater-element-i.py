class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        res = [-1] * len(nums1)
        mapp = {n:i for i, n in enumerate(nums1)}
        for i in range(len(nums2)-1, -1, -1):
            curr = nums2[i]
            while stack and stack[-1] < curr:
                stack.pop()
            if stack and curr in mapp:
                res[mapp[curr]] = stack[-1]
            stack.append(curr)
        return res

        
        