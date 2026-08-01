class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ans = 1
        for i in range(len(points)):
            a = points[i]
            count = collections.defaultdict(int)
            for j in range(i+1, len(points)):
                b = points[j]
                if b[0] == a[0]:
                    slope = float('inf')
                else:
                    slope = (b[1]-a[1]) / (b[0]-a[0])
                count[slope] += 1
                ans = max(ans, count[slope] + 1)
        return ans