class Solution:
    def minOperations(self, logs: List[str]) -> int:
        log = "".join(logs)
        log = log.split('/')
        stack = []
        for i in log:
            if i == '..' and stack:
                stack.pop()
            elif i == '.':
                continue
            elif i != '..':
                stack.append(i)
        return len(stack)- 1 