class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)

        if ra == rb:
            return False

        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra

        self.parent[rb] = ra

        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1

        return True
n, m = map(int, input().split())
edges = []

for _ in range(m):
    b, e, w = map(int, input().split())
    edges.append((w, b, e))

edges.sort()

dsu = DSU(n)

mst_weight = 0
edges_used = 0

for w, u, v in edges:
    if dsu.union(u, v):
        mst_weight += w
        edges_used += 1

        if edges_used == n - 1:
            break
print(mst_weight)