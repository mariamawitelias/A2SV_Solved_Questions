class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = Counter(nums)
        idx = 0
        for color in range(3):
            freq = count.get(color, 0)
            nums[idx : idx + freq] = [color] * freq
            idx += freq