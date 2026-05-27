N = int(input())

activities = [tuple(map(int, input().split())) for _ in range(N)]

memo = {}

def dp(day, last):
    # finished all days
    if day == N:
        return 0

    if (day, last) in memo:
        return memo[(day, last)]

    ans = 0

    for activity in range(3):
        if activity != last:
            ans = max(
                ans,
                activities[day][activity] + dp(day + 1, activity)
            )

    memo[(day, last)] = ans
    return ans

# last = -1 means no previous activity
print(dp(0, -1))