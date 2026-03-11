class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        mini = [0] * len(nums)
        for i in range(len(nums)):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            if not stack:
                mini[i] = -1
            else:
                mini[i] = stack[0]
            stack.append(i)
        stack = []
        for twoIdx in range(len(nums)):
            while stack and nums[stack[-1]] <= nums[twoIdx]:
                stack.pop()
            if stack:
                threeIdx = stack[-1]
                oneIdx = mini[threeIdx]
                if oneIdx != -1 and nums[oneIdx] < nums[twoIdx]:
                    return True
            stack.append(twoIdx)
        return False