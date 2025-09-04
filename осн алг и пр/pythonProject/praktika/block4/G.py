for _ in range(int(input())):
    n, H = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort()
    max1 = a[-1]
    max2 = a[-2]

    damage = max1 + max2
    d = H // damage
    ost = H % damage
    count = d * 2

    if ost > 0:
        if ost <= max1:
            count += 1
        else:
            count += 2

    print(count)