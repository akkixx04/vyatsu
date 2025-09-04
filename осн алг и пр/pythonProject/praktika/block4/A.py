import math
for _ in range(int(input())):
    l, r = map(int, input().split())
    n = (1 + math.isqrt(1 + 8 * (r - l))) // 2
    print(n)