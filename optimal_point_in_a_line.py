n = int(input())
a = list(map(int, input().split()))
a.sort()
mid = len(a) // 2
if len(a) % 2 == 0:
    print(a[mid - 1])  
else:
    print(a[mid])      
