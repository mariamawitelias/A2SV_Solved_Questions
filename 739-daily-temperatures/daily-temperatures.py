class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            curr = temperatures[i]
            while stack and temperatures[stack[-1]] < curr:
                top = stack.pop()
                res[top] = i - top
            stack.append(i)
        return res 
        
