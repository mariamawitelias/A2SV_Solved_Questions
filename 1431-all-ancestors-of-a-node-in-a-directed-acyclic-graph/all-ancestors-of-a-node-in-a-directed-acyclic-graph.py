class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)
        q = deque()
        for fro, to in edges:
            adj[to].append(fro)
        
        ans = []
        for node in range(n):
            ancestor = set()
            q.append(node)
            while q:
                node = q.popleft()
                for i in adj[node]:
                    if i not in ancestor:
                        ancestor.add(i)
                        q.append(i)
            ans.append(sorted(ancestor))
        return ans
                    

