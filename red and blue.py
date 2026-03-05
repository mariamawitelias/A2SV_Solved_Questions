t = int(input())
for _ in range(t):
    n = int(input())
    r = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    pre1, pre2 = [0], [0]
    prer, preb = 0, 0
    res = 0
    for i in r:
        prer += i
        pre1.append(prer)
    for i in b:
        preb += i
        pre2.append(preb)
    maxi1 = max(pre1)
    maxi2 = max(pre2)
    print(max(0, maxi1 + maxi2))
    
    
    

