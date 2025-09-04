t = int(input())
for i in range(t):
    a, b , n = map(int, input().split())
    time_instrument = list(map(int, input().split()))
    for i in time_instrument:
        b += min(i, a - 1)
    print(b)