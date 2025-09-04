import math
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    k = int(math.sqrt(s))
    if k ** 2 == s:
        print("YES")
    else:
        print("NO")
