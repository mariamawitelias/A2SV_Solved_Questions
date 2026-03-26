from collections import Counter
n = int(input())
tree = [[] for _ in range(n)]
for i in range(1, n):
    node = int(input())
    tree[node-1].append(i)
for node in range(n):
    if len(tree[node]) > 0:
        count = 0
        for i in tree[node]:
            if len(tree[i]) == 0:
                count += 1
        if count < 3:
            print("No")
            break
else:
    print("Yes")