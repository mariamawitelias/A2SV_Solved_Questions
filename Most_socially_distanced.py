t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    res = []
    res.append(p[0]) 
    for i in range(1, n-1):
        diff1 = p[i] - p[i-1]
        diff2 = p[i+1] - p[i]
        if diff1 * diff2 < 0:
            res.append(p[i])
    res.append(p[n-1]) 
    print(len(res))
    print(*res)
