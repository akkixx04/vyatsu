t = int(input())
for _ in range(t):
    x1, x2, x3 = map(int, input())
    x = [x1,x2,x3]
    sorted(x)
    m = x[1]
    f = abs(x1-m) + abs(x2-m) + abs(x3-m)
    print(f)