class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set([0])
        q = deque([0])
        while q:
            n = q.popleft()
            for neigh in rooms[n]:
                if neigh not in visited:
                    q.append(neigh)
                    visited.add(neigh)
        return len(visited) == len(rooms)