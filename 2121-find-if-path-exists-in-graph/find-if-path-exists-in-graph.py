class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = set()
        mapp = defaultdict(list)
        for i, j in edges:
            mapp[i].append(j)
            mapp[j].append(i)
        def dfs(node, visited):
            if node == destination:
                return True
            visited.add(node)
            for v in mapp[node]:
                if v not in visited:
                    visited.add(v)
                    found = dfs(v, visited)
                    if found:
                        return True
            return False
        return dfs(source, visited)
        