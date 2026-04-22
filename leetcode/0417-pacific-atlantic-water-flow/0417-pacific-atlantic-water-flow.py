class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def inbound(r, c):
            return 0 <= r < len(heights) and 0 <= c < len(heights[0])
        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        pas, at = set(), set()
        res = []
        def dfs(r, c, visited, prev):
            if not inbound(r, c):
                return
            if (r,c) in visited:
                return
            if heights[r][c] < prev:
                return
            visited.add((r,c))
            for ro, col in direction:
                newr = ro + r
                newc = col + c
                dfs(newr, newc, visited, heights[r][c])   
        for c in range(len(heights[0])):
            dfs(0, c, pas, heights[0][c])
            dfs(len(heights)-1, c, at, heights[len(heights)-1][c])
        for r in range(len(heights)):
            dfs(r, 0, pas, heights[r][0])
            dfs(r, len(heights[0])-1, at, heights[r][len(heights[0])-1])
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if (r, c) in pas and (r, c) in at:
                    res.append([r,c])
        return res

                
