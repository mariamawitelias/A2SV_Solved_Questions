class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res = ""
        for i in s:
            if i == ']':
                char = ""
                while stack and stack[-1] != '[':
                    a = stack.pop()
                    char = a + char
                stack.pop()
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(char * int(k))
            else:
                stack.append(i)
        return "".join(stack)