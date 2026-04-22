t = int(input())
for _ in range(t):
    m = int(input())
    p = list(map(int, input().split()))
    
    def dfs(arr, level):
        if len(arr) == 1:
            return 0
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        left_min, left_max = min(left), max(left)
        right_min, right_max = min(right), max(right)
        if (left_max - left_min + 1 != len(left) or 
            right_max - right_min + 1 != len(right)):
            return -1
        if left_max < right_min:
            res1 = dfs(left, level + 1)
            res2 = dfs(right, level + 1)
            if res1 == -1 or res2 == -1:
                return -1
            return res1 + res2
        elif right_max < left_min:
            res1 = dfs(right, level + 1)
            res2 = dfs(left, level + 1)
            if res1 == -1 or res2 == -1:
                return -1
            return 1 + res1 + res2
        else:
            return -1
    result = dfs(p, 0)
    print(result)