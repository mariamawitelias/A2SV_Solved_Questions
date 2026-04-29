class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adj = defaultdict(list)
        indeg = [0] * (n+1)
        q = deque()
        for fro, to in relations:
            adj[fro].append(to)
            indeg[to] += 1
        for i in range(1, n + 1):
            if indeg[i] == 0:
                q.append(i)
        month = [0] * (n + 1)
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                month[node] += time[node - 1]
                for lij in adj[node]:
                    indeg[lij] -= 1
                    if indeg[lij] == 0:
                        q.append(lij)
                    month[lij] = max(month[lij], month[node])
        return max(month)
            
            
        