t = int(input())
for i in range(t):
    l1, r1 = map(int, input().split())
    l2, r2 = map(int, input().split())
    s = max(l1, l2)
    k = min(r1, r2)
    if s > k:
        i = 1
    else:
        i = (k - s) + 2
        if l1 == l2:
            i -= 1
        if r1 == r2:
            i -= 1
    print(i)