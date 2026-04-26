class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh, time = 0, 0
        direction = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        n, m = len(grid), len(grid[0])
        q = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append([i, j])

        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in direction:
                    newr = r + dr
                    newc = c + dc

                    if newr < 0 or newr == n or newc < 0 or newc == m or grid[newr][newc] != 1:
                        continue

                    grid[newr][newc] = 2
                    q.append([newr, newc])
                    fresh -= 1

            time += 1

        return time if fresh == 0 else -1