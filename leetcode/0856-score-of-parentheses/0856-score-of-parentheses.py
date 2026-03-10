class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        top = 0
        for i in s:
            if i == '(':
                stack.append(i)
            else:
                if stack and stack[-1] == '(':
                    stack.pop()
                    stack.append(1)
                else:
                    top = 0
                    while stack and stack[-1] != '(':
                        a = stack.pop()
                        top += a
                    stack.pop()
                    stack.append(2*top)
        return sum(stack)
