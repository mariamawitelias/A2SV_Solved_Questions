n, k = map(int, input().split())
a = list(map(int, input().split()))
window = {}
res = 0
l = 0
for r in range(n):
    window[a[r]] = window.get(a[r], 0) + 1
    while len(window) > k:
        window[a[l]] -= 1
        if window[a[l]] == 0:
            del window[a[l]]   
        l += 1
    res += (r - l + 1)
print(res)
