a, b = map(int, input().split())
res = []
while b > a:
    res.append(b)
    if b % 2 == 0:
        b //= 2
    elif b % 10 == 1:
        b //= 10
    else:
        print("NO")
        break
else:
    if b == a:
        res.append(a)
        res.reverse()
        print("YES")
        print(len(res))
        print(*res)
    else:
        print("NO")
