class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        arr = []
        for q, w in zip(quality, wage):
            arr.append([w/q, q])
        arr.sort()
        h = []
        for i in range(k):
            h.append(-arr[i][1])
        heapify(h)
        tot = -sum(h)
        wage = tot * arr[k-1][0]
        for i in range(k, len(arr)):
            tot += heappop(h)
            tot += arr[i][1]
            heappush(h, -arr[i][1])
            wage = min(wage, tot * arr[i][0])
        return wage