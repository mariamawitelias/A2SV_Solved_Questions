class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        white = 1
        gray = 2
        black = 3
        mapp = defaultdict(list)
        for i, j in prerequisites:
            mapp[i].append(j)
        color = {k: white for k in range(numCourses)}
        no = True
        def dfs(node):
            nonlocal no
            if not no:
                return
            color[node] = gray
            for v in mapp[node]:
                if color[v] == white:
                    dfs(v)
                elif color[v] == gray:
                    no = False
            color[node] = black
        for node in range(numCourses):
            if color[node] == white:
                dfs(node)
        return no