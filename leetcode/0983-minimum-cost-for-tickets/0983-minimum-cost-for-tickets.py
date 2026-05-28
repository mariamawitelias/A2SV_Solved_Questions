class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = {}
        def dp(i):
            if i >= len(days):
                return 0
            if i in memo:
                return memo[i]
            cost1 = dp(i+1) + costs[0]
            j = i
            while j < len(days) and days[j] < days[i] + 7:
                j += 1
            cost7 = dp(j) + costs[1]
            while j < len(days) and days[j] < days[i] + 30:
                j += 1
            cost30 = dp(j) + costs[2]
            memo[i] = min(cost1, cost7, cost30)
            return memo[i]
        return dp(0)
