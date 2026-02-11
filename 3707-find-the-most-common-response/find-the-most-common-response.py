class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        new = []
        for i in responses:
            new += set(i)
        count = Counter(new)
        x = max(count.values())
        res = []
        for key in count:
            if count[key] == x:
                res.append(key)
        res.sort()
        return res[0]
            