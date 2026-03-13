class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        count = 1
        pos = points[0][1]
        for start, end in points[1:]:
            if start <= pos:
                continue
            else:
                count += 1
                pos = end
        return count
        
        



        