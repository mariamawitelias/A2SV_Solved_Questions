from collections import defaultdict, deque

n = int(input())
names = [input().strip() for _ in range(n)]
graph = defaultdict(set)
indeg = [0] * 26

for i in range(n - 1):
    s1, s2 = names[i], names[i + 1]
    
    pos = 0
    while pos < len(s1) and pos < len(s2) and s1[pos] == s2[pos]:
        pos += 1
    if pos == len(s1) or pos == len(s2):
        if pos == len(s2):
            print("Impossible")
            exit()
        continue
    
    u = ord(s1[pos]) - ord('a')
    v = ord(s2[pos]) - ord('a')
    
    if v not in graph[u]:
        graph[u].add(v)
        indeg[v] += 1

q = deque()
for i in range(26):
    if indeg[i] == 0:
        q.append(i)

result = []
while q:
    u = q.popleft()
    result.append(chr(u + ord('a')))
    for v in graph[u]:
        indeg[v] -= 1
        if indeg[v] == 0:
            q.append(v)
if len(result) != 26:
    print("Impossible")
else:
    print(''.join(result))