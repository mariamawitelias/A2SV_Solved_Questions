class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l, r = 1, len(nums)-1
        while l < r:
            mid = (l+r)//2
            count = 0
            for i in range(len(nums)):
                if nums[i] <= mid:
                    count += 1
            if count <= mid:
                l = mid + 1
            else:
                r = mid
        return l