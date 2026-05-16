class MedianFinder:

    def __init__(self):
        self.sm, self.large = [], []
        heapify(self.sm)
        heapify(self.large)
    def addNum(self, num: int) -> None:
        heappush(self.sm, -num)
        if self.sm and self.large and (-self.sm[0] > self.large[0]):
            val = -heappop(self.sm)
            heappush(self.large, val)
        if len(self.sm) > len(self.large) + 1:
            val = -heappop(self.sm)
            heappush(self.large, val)
        if len(self.large) > len(self.sm) +1:
            val = -heappop(self.large)
            heappush(self.sm, val)

    def findMedian(self) -> float:
        if len(self.sm) > len(self.large):
            return -self.sm[0]
        elif len(self.large) > len(self.sm):
            return self.large[0]
        else:
            return (-self.sm[0] + self.large[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()