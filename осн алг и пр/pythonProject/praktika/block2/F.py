t = int(input())
for i in range(t):
    a, b, c, d = map(int, input().split())
    if a > b:
        a, b = b, a
    if c > d:
        c, d = d, c
    if (a < c < b < d) or (c < a < d < b):
        print("YES")
    else:
        print("NO")