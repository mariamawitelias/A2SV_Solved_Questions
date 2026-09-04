class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        if minutes == len(customers):
            return sum(customers)
        res = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                res += customers[i]
        win = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                win += customers[i]
        maxi = win
        left = 0
        right = minutes - 1

        l = 0
        for r in range(minutes, len(customers)):
            if grumpy[r] == 1:
                win += customers[r]
            if grumpy[l] == 1:
                win -= customers[l]
            l += 1
            if win > maxi:
                maxi = win
                left = l
                right = r

        return res + maxi