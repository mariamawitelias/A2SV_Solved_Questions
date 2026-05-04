class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque()
        direction = [[-1,0], [1,0], [0,-1], [0,1]]
        res = -1
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    q.append([i, j])
        while q:
            r, c = q.popleft()
            res = grid[r][c]
            for dr, dc in direction:
                newr, newc = r+dr, c+dc
                if 0 <= newr < n and 0 <= newc < n and grid[newr][newc] == 0:
                    q.append([newr, newc])
                    grid[newr][newc] = grid[r][c] + 1
        return res - 1 if res > 1 else -1 