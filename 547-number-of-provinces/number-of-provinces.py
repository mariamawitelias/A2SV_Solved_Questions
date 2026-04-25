class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj = defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j] == 1:
                    adj[i].append(j)
        visited = set()
        def dfs(node, visited):
            if node in visited:
                return
            visited.add(node)
            for neigh in adj[node]:
                dfs(neigh, visited)
        res = 0
        for i in range(len(isConnected)):
            if i not in visited:
                res += 1
                dfs(i, visited)
        return res

            
        

        