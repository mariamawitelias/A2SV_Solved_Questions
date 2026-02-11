t = int(input())

for _ in range(t):
    n, x, k = map(int, input().split())
    s = input().strip()
    for i in range(n):
        if s[i] == 'L':
            x -= 1
        else:
            x += 1

        k -= 1
        if x == 0:
            break

    ans = 0
    if x == 0:
        ans = 1
        for i in range(n):
            if s[i] == 'L':
                x -= 1
            else:
                x += 1

            if x == 0:
                ans += k // (i + 1)
                break

    print(ans)
