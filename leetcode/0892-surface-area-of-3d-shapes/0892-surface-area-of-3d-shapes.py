class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        
        l = len(grid)
        area=0
        for row in range(l):
            for col in range(l):
                if grid[row][col]:
                    area += (grid[row][col]*4) +2 
                if row:
                    area -= min(grid[row][col],grid[row-1][col])*2
                if col: 
                    area -= min(grid[row][col],grid[row][col-1])*2
        return area