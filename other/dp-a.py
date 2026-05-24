n = int(input())
h = list(map(int, input().split()))
memo = {}
def dp(i):
    if i == 0:
        return 0
    if i == 1:
        return abs(h[1] - h[0])
    if i not in memo:
        one_jump = dp(i - 1) + abs(h[i] - h[i - 1])
        two_jump = dp(i - 2) + abs(h[i] - h[i - 2])
        memo[i] = min(one_jump, two_jump)
    return memo[i]
print(dp(n - 1))