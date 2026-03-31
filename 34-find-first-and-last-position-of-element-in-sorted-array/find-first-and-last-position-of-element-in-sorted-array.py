from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                left = mid
                right = mid
                while left - 1 >= 0 and nums[left - 1] == target:
                    left -= 1
                while right + 1 < len(nums) and nums[right + 1] == target:
                    right += 1
                return [left, right]
        return [-1, -1]