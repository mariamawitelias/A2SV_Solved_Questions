class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        q = deque()
        q.append(["0000", 0])
        visited = set(deadends)
        def children(n):
            res = []
            for i in range(4):
                digit = str((int(n[i])+1) % 10)
                res.append(n[:i] + digit + n[i+1:])
                digit = str((int(n[i])-1+10) % 10)
                res.append(n[:i] + digit + n[i+1:])
            return res
        while q:
            n, turn = q.popleft()
            if n == target:
                return turn
            for child in children(n):
                if child not in visited:
                    q.append([child, turn+1])
                    visited.add(child)
        return -1