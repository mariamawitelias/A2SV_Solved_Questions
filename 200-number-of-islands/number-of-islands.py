class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def inbound(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])
        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = [[False] * len(grid[0]) for i in range(len(grid))]
        res = 0
        def dfs(r, c):
            if not inbound(r, c):
                return
            if grid[r][c] == "0":
                return
            if visited[r][c]:
                return
            visited[r][c] = True
            for ro, col in direction:
                newr = r + ro
                newc = c + col
                dfs(newr, newc)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and not visited[r][c]:
                    res += 1
                    dfs(r, c)
        return res
