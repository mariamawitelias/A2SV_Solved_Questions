class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hashh = {0:-1}
        prefix = 0
        for i in range(len(nums)):
            prefix += nums[i]
            if prefix % k not in hashh:
                hashh[prefix%k] = i
            else:
                if i - hashh[prefix%k] > 1:
                    return True
        return False

