matrix = []
for _ in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)
res = 0
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            if (i + 1) != 3:
                res += abs(i + 1 - 3)
            if (j + 1) != 3:
                res += abs(j + 1 - 3)
print(res)

