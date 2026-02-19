class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        arrow = 1
        points.sort(key=lambda x: x[1])
        arrow_pos = points[0][1] 
        for start, end in points[1:]: 
            if start <= arrow_pos: 
                continue 
            else:  
                arrow += 1 
                arrow_pos = end
        return arrow
        
        



        