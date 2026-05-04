class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        n = len(maze)
        m = len(maze[0])
        q = deque()
        direction = [[-1,0], [1,0], [0,-1], [0,1]]
        q.append(entrance)
        res = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if (r != entrance[0] or c != entrance[1]) and (
                    r == 0 or r == n - 1 or c == 0 or c == m - 1
                ):
                    return res
                for dr, dc in direction:
                    newr, newc = r+dr, c+dc
                    if 0 <= newr < n and 0 <= newc < m and maze[newr][newc] == ".":
                        maze[newr][newc] = "+"
                        q.append([newr, newc])
            res += 1
        return -1
        

