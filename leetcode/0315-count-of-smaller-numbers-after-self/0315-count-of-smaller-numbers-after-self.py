class Solution:
    def countSmaller(self, nums):
        ans = [0] * len(nums)
        def mergesort(l, r):
            if l == r:
                return [[nums[l], l]]
            mid = (l + r) // 2
            left = mergesort(l, mid)
            right = mergesort(mid + 1, r)
            tmp = [num for num, idx in right]
            for num, idx in left:
                i = bisect_left(tmp, num)
                ans[idx] += i
            return sorted(left + right)
        mergesort(0, len(nums) - 1)
        return ans



