class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        res = []
        for inter in intervals:
            if not res or res[-1][1] < inter[0]:
                res.append(inter)
            else:
                res[-1][1] = max(res[-1][1], inter[1])
        return res


        