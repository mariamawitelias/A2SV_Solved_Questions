class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        pre = 0
        for i in nums:
            pre += i
            self.prefix.append(pre)
    def sumRange(self, left: int, right: int) -> int:
        l = self.prefix[left-1] if left > 0 else   0
        res = self.prefix[right] - l
        return res
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)