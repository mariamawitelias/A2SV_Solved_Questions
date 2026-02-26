n, s = map(int, input().split())
a = list(map(int, input().split()))
window = 0
res = 0
l = 0
for r in range(n):
    window += a[r]
    while window >= s:
        res += n - r
        window -= a[l]
        l += 1       
print(res)
