class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minq = deque()
        maxq = deque()
        start = 0
        res = 0
        for end in range(len(nums)):
            while minq and minq[-1] < nums[end]:
                minq.pop()
            minq.append(nums[end])
            while maxq and maxq[-1] > nums[end]:
                maxq.pop()
            maxq.append(nums[end])
            while abs(maxq[0] - minq[0]) > limit:
                if maxq[0] == nums[start]:
                    maxq.popleft()
                if minq[0] == nums[start]:
                    minq.popleft()
                start += 1
            res = max(res, end - start + 1)
        return res
