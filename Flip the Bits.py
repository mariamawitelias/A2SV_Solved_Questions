t = int(input())
for _ in range(t):
    n = int(input())
    a = input()
    b = input()
    balanced = [False] * n
    zero = 0
    one = 0
    for i in range(n):
        if a[i] == '0':
            zero += 1
        else:
            one += 1
        if zero == one:
            balanced[i] = True
    flip = 0
    possible = True
    for i in range(n-1, -1, -1):
        bit = a[i]
        if flip:
            bit = '1' if bit == '0' else '0'
        if bit != b[i]:
            if not balanced[i]:
                possible = False
                break
            flip ^= 1
    print("YES" if possible else "NO")
