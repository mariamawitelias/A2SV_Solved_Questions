class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        order = []
        inc = [0] * numCourses
        q = deque()
        for i, n in prerequisites:
            adj[n].append(i)
            inc[i] += 1
        for i in range(numCourses):
            if inc[i] == 0:
                q.append(i)
        while q:
            n = q.popleft()
            order.append(n)
            for neigh in adj[n]:
                inc[neigh] -= 1
                if inc[neigh] == 0:
                    q.append(neigh)

        if len(order) == numCourses:
            return order
        return []
