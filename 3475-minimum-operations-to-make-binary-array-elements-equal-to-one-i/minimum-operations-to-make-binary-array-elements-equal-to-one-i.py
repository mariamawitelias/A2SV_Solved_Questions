class Solution:
    def minOperations(self, nums: List[int]) -> int:
        l = 0
        res = 0
        q = deque(nums[:3])
        if q[0] == 0:
            for i in range(3):
                q[i] = 1 - q[i] 
            res += 1
        for r in range(3, len(nums)):
            q.append(nums[r])
            q.popleft()
            if q[0] == 0:
                for i in range(3):
                    q[i] = 1 - q[i]
                res += 1
        if 0 in q:
            return -1
        return res