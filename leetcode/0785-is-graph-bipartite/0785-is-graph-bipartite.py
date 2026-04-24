class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1 for _ in range(len(graph))]
        res = True
        def dfs(node, graph):
            temp = True
            for neighbour in graph[node]:
                if color[neighbour] == -1:
                    if color[node] == 0:
                        color[neighbour] = 1
                    else:
                        color[neighbour] = 0
                    temp = temp and dfs(neighbour, graph)
                elif color[neighbour] == color[node]:
                    return False
            return temp
        for node in range(len(graph)):
            if color[node] == -1:
                color[node] = 0
                res = res and dfs(node, graph)
        return res