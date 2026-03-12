class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        nextSmaller = [len(heights)] * len(heights)
        previousSmaller = [-1] * len(heights)
        stack = []
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                top = stack.pop()
                nextSmaller[top] = i
            if stack:
                previousSmaller[i] = stack[-1]
            stack.append(i)
        maxi = 0
        for i in range(len(heights)):
            curr = heights[i]
            width = nextSmaller[i] - previousSmaller[i] - 1
            maxi = max(maxi, curr*width)
        return maxi

        