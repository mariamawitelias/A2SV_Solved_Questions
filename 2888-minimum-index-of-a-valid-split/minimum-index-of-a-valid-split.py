class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        count = Counter(nums)
        x = len(nums) // 2
        for k, v in count.items():
            if v > x:
                dom, count = k, v
                break
        l = 0
        for i in range(len(nums)-1):
            if nums[i] == dom:
                l += 1 
            left = i + 1
            right = len(nums) - left
            r = count - l
            if l > left // 2 and r > right // 2:
                return i
        return -1


        
        