r1, c1, r2, c2 = map(int, input().split())

if r1 == r2 or c1 == c2:
    l = 1
else:
    l = 2

if (r1 + c1) % 2 != (r2 + c2) % 2:
    s = 0
elif abs(r1 - r2) == abs(c1 - c2):
    s = 1
else:
    s = 2

k = max(abs(r1 - r2), abs(c1 - c2))

print(l, s, k)