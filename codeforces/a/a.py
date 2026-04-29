from collections import deque
n = int(input())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)
arr = [0] * (n + 1)
def bfs(node, par):
    arr[node] = 0
    q = deque()
    q.append((node, par))
    while q:
        node, par = q.popleft()
        for lij in tree[node]:
            if lij != par:
                arr[lij] = arr[node] + 1
                q.append((lij, node))
bfs(1, 0)
bfs(arr.index(max(arr)), 0)
print(3 * max(arr))