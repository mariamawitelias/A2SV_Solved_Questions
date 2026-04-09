import bisect
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b.sort()
    prev = -float('inf')
    flag = True
    for n in a:
        choose = float('inf')
        if n >= prev:
            choose = min(choose, n)
        num = prev + n
        i = bisect.bisect_left(b, num)
        if i < m:
            ch = b[i] - n
            if ch >= prev:
                choose = min(choose, ch)
        if choose == float('inf'):
            flag = False
            break
        prev = choose
    if flag:
        print("YES")
    else:
        print("NO")