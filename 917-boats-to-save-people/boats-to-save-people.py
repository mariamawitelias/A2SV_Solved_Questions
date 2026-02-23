class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        res = 0
        people.sort()
        count = len(people)
        i, j = 0, len(people)-1
        while i < j:
            if people[i] + people[j] > limit:
                j -= 1
            else:
                res += 1
                i += 1
                j -= 1
                count -= 2
        return res + count



        