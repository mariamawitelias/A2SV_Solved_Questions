class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-p for p in stones]
        heapify(h)
        while len(h) > 1:
            x = -heappop(h)
            y = -heappop(h)
            if x != y:
                heappush(h, -(x-y))
        return -h[0] if h else 0