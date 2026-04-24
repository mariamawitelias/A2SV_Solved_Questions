class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        mapp = {i:graph[i] for i in range(len(graph))}
        res = []
        def dfs(node, path):
            path.append(node)
            if node == len(graph) - 1:
                res.append(path[:])               
            for neigh in mapp[node]:
                dfs(neigh, path)
                path.pop()
        dfs(0, [])
        return res



        