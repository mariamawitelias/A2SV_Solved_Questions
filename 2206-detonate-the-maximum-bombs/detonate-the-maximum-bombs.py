class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        mapp = defaultdict(list)
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i == j: continue
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]
                dis = sqrt((x2 - x1)**2 + (y2 - y1)**2)
                if dis <= r1:
                    mapp[i].append(j)
                    
        def dfs(node, visited):
            if node in visited:
                return
            visited.add(node)
            for neigh in mapp[node]:
                dfs(neigh, visited)
            return
        res = 0
        for i in range(len(bombs)):
            cur = set()
            dfs(i, cur)
            res = max(res, len(cur))
        return res




        
