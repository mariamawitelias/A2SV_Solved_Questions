n, k = map(int, input().split())
a = list(map(int, input().split()))
table = {}
l = 0
res = 0
for r in range(n):
    table[a[r]] = table.get(a[r], 0) + 1
    while len(table) > k:
        table[a[l]] -= 1
        if table[a[l]] == 0:
            del table[a[l]]
        l += 1
    cur = r - l + 1
    if cur > res:
        res = cur
        left = l
        right = r    
print(left+1, right+1)
