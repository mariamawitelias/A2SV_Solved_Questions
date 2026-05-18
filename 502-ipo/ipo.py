class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        project = [[capital[i], profits[i]] for i in range(len(profits))]
        project.sort()
        h = []
        i = 0
        while k > 0:
            while i < len(profits) and project[i][0] <= w:
                heappush(h, -project[i][1])
                i += 1
            if not h:
                break
            w -= heappop(h)
            k -= 1
        return w
