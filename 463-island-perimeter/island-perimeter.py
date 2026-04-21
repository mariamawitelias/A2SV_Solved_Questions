class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def inbound(r, c):
            return 0<= r < len(grid) and 0 <= c < len(grid[0])
        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = [[False] * len(grid[0]) for i in range(len(grid))]
        def dfs(r, c):
            if not inbound(r, c):
                return 1
            if grid[r][c] == 0:
                return 1
            if visited[r][c]:
                return 0
            visited[r][c] = True
            perm = 0
            for rchange, cchange in direction:
                newr = r + rchange
                newc = c + cchange
                perm += dfs(newr, newc)
            return perm
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i, j)
        return 0

            