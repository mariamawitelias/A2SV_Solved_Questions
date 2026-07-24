class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
       
        xy_area = sum(1 for row in grid for val in row if val > 0)
        yz_area = sum(max(row) for row in grid)
        
        zx_area = sum(max(col) for col in zip(*grid))
        
        return xy_area + yz_area + zx_area        