n, k, q = map(int, input().split())
ranges = []
c = [0] * (200000 + 2)
for _ in range(n):
    l, r = map(int, input().split())
    c[l] += 1
    c[r+1] -= 1
for i in range(1, 200000+1):
    c[i] += c[i-1]
for i in range(1, 200000+1):
    if c[i] >= k:
        c[i] = 1
    else:
        c[i] = 0
for i in range(1, 200000+1):
    c[i] += c[i-1]
for _ in range(q):
    a, b = map(int, input().split())
    print(c[b] - c[a-1])
