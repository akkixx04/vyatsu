t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if n == 1:
        print("NO")
    elif sum(a) <= 6:
        print("NO")
    else:
        print("YES")