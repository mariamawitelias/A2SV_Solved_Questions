class Solution:
    def countSmaller(self, nums):
        ans = [0] * len(nums)
        def merge(left, right):
            res = []
            l, r = 0, 0
            while l < len(left) and r < len(right):
                if left[l][0] <= right[r][0]:
                    res.append(left[l])
                    l += 1
                else:
                    res.append(right[r])
                    r += 1
            res.extend(left[l:])
            res.extend(right[r:])
            return res

        def calc(left, right):
            tmp = [num for num, idx in right]
            for num, idx in left:
                i = bisect_left(tmp, num)
                ans[idx] += i

        
        def divide(l, r):
            if l == r:
                return [[nums[l], l]]
            mid = (l + r) // 2
            left = divide(l, mid)
            right = divide(mid + 1, r)
            calc(left, right)
            return merge(left, right)
        
        divide(0, len(nums) - 1)
        return ans



