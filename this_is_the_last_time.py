t = int(input())
for _ in range(t):
    n, k = map(int, input().split()) 
    p = []
    for _ in range(n):
        a, b, c = map(int, input().split())
        p.append((a, b, c))
    p.sort()
    cur = k
    for a, b, c in p:
        if a > cur:
            break
        cur = max(cur, c)
    
    print(cur)
