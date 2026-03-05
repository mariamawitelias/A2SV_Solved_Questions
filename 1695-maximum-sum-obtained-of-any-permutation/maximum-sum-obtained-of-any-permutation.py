class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 10**9 + 7
        prefix = [0] * (len(nums) + 1)
        for start, end in requests:
            prefix[start] += 1
            prefix[end + 1] -= 1
        pre = 0
        for i, n in enumerate(prefix):
            pre += n
            prefix[i] = pre
        res = 0
        nums.sort(reverse = True)
        freq = sorted(prefix[:-1], reverse = True)
        for i in range(len(nums)):
            res = (res + freq[i] * nums[i]) % MOD
        return res


        