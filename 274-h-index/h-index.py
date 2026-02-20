class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        mp = {}
        lis = [i for i in range(1, n+1)]
        for i in range(len(lis)):
            count = 0
            for j in citations:
                if lis[i] <= j:
                    count += 1
            mp[lis[i]] = count
        res = 0
        for k, v in mp.items():
            if v >= k:
                res = max(res, k)
        return res 
                        



        