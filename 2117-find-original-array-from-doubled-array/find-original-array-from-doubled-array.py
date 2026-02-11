class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        res = []
        if len(changed) % 2 != 0:
            return []
        changed.sort()
        c = Counter(changed)
        for i in changed:
            if i in c and c[i] >= 1:
                c[i] -= 1
                if i * 2 in c and c[(i * 2)] >= 1:
                    res.append(i)
                    c[i * 2] -= 1
            if len(res) == len(changed) // 2:
                return res
        return []

        
        