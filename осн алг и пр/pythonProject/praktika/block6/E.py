t = int(input())

for _ in range(t):
    n = int(input())
    m = [[0] * n for _ in range(n)]
    for i in range(n):
        row = input()
        for j in range(n):
            m[i][j] = int(row[j])

    res = "YES"
    for i in range(n - 2, -1, -1):
        for j in range(n - 2, -1, -1):
            if m[i][j] and not m[i + 1][j] and not m[i][j + 1]:
                res = "NO"

    print(res)