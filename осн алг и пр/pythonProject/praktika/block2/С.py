t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    k = 1
    S = 0
    for i in a:
        S += k * i
        k *= -1
    print(S)

