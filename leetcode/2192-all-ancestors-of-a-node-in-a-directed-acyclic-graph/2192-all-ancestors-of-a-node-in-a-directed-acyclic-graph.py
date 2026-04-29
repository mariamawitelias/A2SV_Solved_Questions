class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)
        indeg = [0] * n
        q = deque()
        for fro, to in edges:
            adj[fro].append(to)
            indeg[to] += 1
        
        ans = [set() for _ in range(n)]
        for node in range(n):
            if indeg[node] == 0:
                q.append(node)
        while q:
            node = q.popleft()
            for lij in adj[node]:
                indeg[lij] -= 1
                if indeg[lij] == 0:
                    q.append(lij)
                ans[lij].add(node)
                ans[lij] |= ans[node]
                # for myancestor in ans[node]:
                #     ans[lij].add(myancestor)
        return [sorted(a) for a in ans]
