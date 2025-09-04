import math
t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    operations = (n + k - 3) //(k - 1)
    print(operations)

