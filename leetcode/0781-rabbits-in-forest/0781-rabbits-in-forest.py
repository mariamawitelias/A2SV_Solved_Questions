class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        ans = Counter(answers)
        count = 0
        for k,v in ans.items():
            if k == 0:
                count += v
            elif v > k+1:
                if 0 < v % (k+1) < k+1:
                    a = 1
                else:
                    a = v % (k + 1)
                b = v // (k+1)
                count += (k+1) * (a+b)
            else:
                count += k + 1      
        return count
