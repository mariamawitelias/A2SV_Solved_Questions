class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, t in enumerate(tasks):
            t.append(i)
        tasks.sort(key = lambda t : t[0] )
        i, time = 0, tasks[0][0]
        h, res = [], []
        while h or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heappush(h, [tasks[i][1], tasks[i][2]])
                i += 1
            if not h:
                time = tasks[i][0]
            else:
                pro, inx = heappop(h)
                time += pro
                res.append(inx)
        return res
