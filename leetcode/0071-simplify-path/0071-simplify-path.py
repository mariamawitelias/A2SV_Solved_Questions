class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for ch in path.split("/"):
            if ch == "." or ch == '':
                continue
            elif ch == ".." and stack:
                stack.pop()
            elif ch != "..":
                stack.append(ch)
        return "/" + "/".join(stack)