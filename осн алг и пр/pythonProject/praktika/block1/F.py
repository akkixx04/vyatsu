t = int(input())
while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    b = sorted(a)
    e = False
    for i in range(n):
        if a[i] % 2 != b[i] % 2:
            e = True
            print("NO")
            break
    if not e:
        print("YES")
    t -= 1